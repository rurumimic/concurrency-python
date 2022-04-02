import asyncio


async def hello_world():
    await asyncio.sleep(1)
    print('Hello World')


async def good_evening():
    await asyncio.sleep(1)
    print('Good Evening')


def main():
    print('step: asyncio.get_event_loop()')
    loop = asyncio.get_event_loop()
    try:
        print('step: loop.run_until_complete()')
        asyncio.run(hello_world())
        asyncio.run(good_evening())
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        print('\nstep: loop.close()')
        loop.close()


if __name__ == "__main__":
    main()

'''
step: asyncio.get_event_loop()
step: loop.run_until_complete()
Hello World
Good Evening
^C
step: loop.close()
'''
