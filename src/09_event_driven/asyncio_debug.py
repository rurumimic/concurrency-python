import asyncio
import logging
import time

logging.basicConfig(level=logging.DEBUG)


async def task():
    logging.info('Task coroutine hit')
    time.sleep(1)
    return 'Return Value'


async def main(loop):
    logging.debug('Main function hit')
    await asyncio.wait([loop.create_task(task())])

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.set_debug(True)
    try:
        loop.run_until_complete(main(loop))
    finally:
        loop.close()

'''
DEBUG:asyncio:Using selector: KqueueSelector
DEBUG:root:Main function hit
INFO:root:Task coroutine hit

# loop.set_debug(True)

WARNING:asyncio:Executing 
  <Task finished name='Task-2' coro=<task() done, defined at asyncio_debug.py:8> 
  result='Return Value' created at asyncio_debug.py:15> took 1.001 seconds
DEBUG:asyncio:Close <_UnixSelectorEventLoop running=False closed=False debug=True>
'''
