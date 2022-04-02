import asyncio
import random


async def producer(queue):
    while True:
        await queue.put(random.randint(1, 5))
        await asyncio.sleep(1)


async def consumer(queue):
    while True:
        article_id = await queue.get()
        print(f'Reader consumed News: {article_id}')

if __name__ == "__main__":
    queue = asyncio.Queue()

    loop = asyncio.get_event_loop()
    loop.create_task(producer(queue))
    loop.create_task(consumer(queue))

    try:
        loop.run_forever()
    finally:
        loop.close()

'''
Reader consumed News: 2
Reader consumed News: 2
Reader consumed News: 1
Reader consumed News: 4
Reader consumed News: 2
Reader consumed News: 2
Reader consumed News: 2
Reader consumed News: 5

^C

RuntimeError: Event loop is closed
'''
