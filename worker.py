import asyncio
from temporalio.worker import Worker
from temporalio.client import Client

from workflow import space_mission_workflow
from activities import read_probes


async def main():
    client = await Client.connect("localhost:7233")

    worker = Worker(
        client=client,
        task_queue="space-mission-task-queue",
        workflows=[space_mission_workflow],
        activities=[read_probes],
    )

    print("Worker started. Listening for workflow tasks...")
    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
