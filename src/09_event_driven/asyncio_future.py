import asyncio


async def task(future):
    await asyncio.sleep(1)
    future.set_result('Future has completed')


async def main():
    future = asyncio.Future()
    await asyncio.ensure_future(task(future))
    print(future.result())

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()

'''
Future has completed
'''
