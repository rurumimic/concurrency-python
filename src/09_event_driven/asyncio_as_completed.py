import asyncio
from concurrent.futures import Future, ThreadPoolExecutor


async def task(n):
    return f'task {n}'


async def one(loop):
    print(loop)  # <_UnixSelectorEventLoop running=True closed=False debug=False>
    futures = [loop.create_task(task(i)) for i in range(1, 4)]

    for future in asyncio.as_completed(futures):
        result = await future
        print(result)


async def two(loop):
    print(loop)  # <_UnixSelectorEventLoop running=True closed=False debug=False>
    task4 = asyncio.ensure_future(task(4))

    for future in asyncio.as_completed([task4]):
        result = await future
        print(result)


async def three(loop):
    print(loop)  # <_UnixSelectorEventLoop running=True closed=False debug=False>
    task5 = asyncio.ensure_future(task(5))

    for future in asyncio.as_completed([task5]):
        result = await future
        print(result)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    print(loop)  # <_UnixSelectorEventLoop running=False closed=False debug=False>
    loop.run_until_complete(asyncio.gather(one(loop), two(loop)))
    loop.run_until_complete(asyncio.wait([three(loop)]))
    loop.close()

'''
task 1
task 2
task 3
task 4
task 5
'''
