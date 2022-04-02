import asyncio
import time


async def task():
    print('Simple event loop')
    time.sleep(3)
    print('End task')


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(task())

    loop.close()
    print(loop.is_closed())  # True


if __name__ == "__main__":
    main()

'''
Simple event loop
End task
True
'''
