import queue
import sys
import threading
import time


def worker(queue):
    while True:
        try:
            time.sleep(1)
            raise Exception(
                f'Exception Thrown In Child Thread {threading.current_thread()}')
        except:
            print('worker exception')
            queue.put(sys.exc_info())


q = queue.Queue()

thread = threading.Thread(target=worker, args=(q, ))
thread.start()

while True:
    try:
        print('Queue get()')
        exception = q.get()
    except queue.Empty:
        print('queue is empty')
        pass
    else:
        # (
        #   <class 'Exception'>,
        #   Exception('Exception Thrown In Child Thread
        #     <Thread(Thread-1, started 123145516310528)>'),
        #   <traceback object at 0x10eb31b80>
        # )
        print(exception)
        break
