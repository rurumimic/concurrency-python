'''
https://docs.python.org/3/library/asyncio-task.html
'''

import asyncio


async def task1():
    print('coroutine 1')


# DeprecationWarning:
# "@coroutine" decorator is deprecated since Python 3.8
# use "async def" instead
@asyncio.coroutine
def task2():
    print('coroutine 2')


async def compute(x, y):
    print(f'Compute {x} + {y} ...')
    await asyncio.sleep(1.0)
    return x + y


async def print_sum(x, y):
    result = await compute(x, y)
    print(f'{x} + {y} = {result}')


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(task1())
    loop.run_until_complete(task2())
    loop.run_until_complete(print_sum(1, 2))
    loop.close()


if __name__ == "__main__":
    main()

'''
coroutine 1
coroutine 2

Compute 1 + 2 ...
1 + 2 = 3
'''
