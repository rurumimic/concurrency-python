import asyncio
import time


async def task(lock, n):
    async with lock:
        print(lock)
        print(f'Task {n} has attained lock, modifying variable')
        time.sleep(2)
    print(lock)
    print(f'Task {n} has release the lock')


async def main(loop):
    lock = asyncio.Lock()
    await asyncio.wait([loop.create_task(task(lock, 1)), loop.create_task(task(lock, 2))])

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main(loop))
    finally:
        loop.close()

'''
<asyncio.locks.Lock object at 0x10da36dc0 [locked]>
Task 1 has attained lock, modifying variable

# sleep 2

<asyncio.locks.Lock object at 0x10da36dc0 [unlocked]>
Task 1 has release the lock
<asyncio.locks.Lock object at 0x10da36dc0 [locked]>
Task 2 has attained lock, modifying variable

# sleep 2

<asyncio.locks.Lock object at 0x10da36dc0 [unlocked]>
Task 2 has release the lock
'''
