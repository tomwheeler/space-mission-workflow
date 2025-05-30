from datetime import timedelta
from dataclasses import dataclass
from typing import List
from temporalio import workflow

from activities import read_probes


@dataclass
class Measurement:
    id: int
    timestamp: str
    altitude: str
    location: str
    temperature: str


@workflow.defn
class space_mission_workflow:
    def __init__(self):
        self.status = "idle"
        self.measurements: List[Measurement] = []
        self.return_home = False

    @workflow.signal
    def initiate_return(self):
        self.return_home = True

    @workflow.query
    def get_status(self):
        return {
            "status": self.status,
            "count": len(self.measurements),
            "latest": self.measurements[-1] if self.measurements else None,
        }

    @workflow.run
    async def run(self) -> str:
        self.status = "countdown"
        for t in [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]:
            await workflow.sleep(timedelta(seconds=1))

        self.status = "launched"
        while not self.return_home:
            # Retry data collection if not completed within 30 seconds
            data = await workflow.execute_activity(
                read_probes, start_to_close_timeout=timedelta(seconds=30)
            )
            self.measurements.append(
                Measurement(
                    id=len(self.measurements),
                    timestamp=workflow.now().isoformat(),
                    **data
                )
            )
            self.status = "orbiting"
            # Pause 5 minutes unless requested to return home
            await workflow.wait_condition(
                lambda: self.return_home, timeout=timedelta(minutes=5)
            )

        self.status = "returning"
        return "Mission complete"
