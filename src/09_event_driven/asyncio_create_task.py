import asyncio
import time


async def task(n):
    time.sleep(1)
    print('Processing', n)


async def event():
    for i in range(5):
        asyncio.create_task(task(i))
    print('Completed Tasks')
    await asyncio.sleep(1)


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(event())
    loop.close()


if __name__ == "__main__":
    main()

'''
Completed Tasks

Processing 0
Processing 1
Processing 2
Processing 3
Processing 4
'''
