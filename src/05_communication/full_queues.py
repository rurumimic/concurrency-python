import queue
import threading
import time


def do_work(size):
    print(f'{threading.current_thread()} Append 1 to queue: {size}')


def worker(queue):
    while not queue.full():
        queue.put(1)
        do_work(queue.qsize())


# maxsize <= 0 is infinite size
q = queue.Queue(maxsize=5)

threads = []
for i in range(4):
    thread = threading.Thread(target=worker, args=(q, ))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

'''
<Thread(Thread-1, started 123145377644544)> Append 1 to queue: 1
<Thread(Thread-1, started 123145377644544)> Append 1 to queue: 2
<Thread(Thread-1, started 123145377644544)> Append 1 to queue: 3
<Thread(Thread-1, started 123145377644544)> Append 1 to queue: 4
<Thread(Thread-1, started 123145377644544)> Append 1 to queue: 5
'''
