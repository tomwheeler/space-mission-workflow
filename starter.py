import asyncio
from temporalio.client import Client

from workflow import space_mission_workflow


async def main():
    client = await Client.connect("localhost:7233")

    result = await client.start_workflow(
        space_mission_workflow.run,
        id="launch-space-mission-001",
        task_queue="space-mission-task-queue",
    )

    print(f"Workflow started with ID: {result.id}")


if __name__ == "__main__":
    asyncio.run(main())
