import asyncio

from temporalio.client import Client
from temporalio.worker import Worker

from greeting import GreetSomeone

TASK_QUEUE = "greeting-tasks"

async def main():
    client = await Client.connect("localhost:7233", namespace="default")
    worker = Worker(
        client,
        task_queue=TASK_QUEUE,
        workflows=[GreetSomeone],
    )
    print("Starting worker...")
    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
