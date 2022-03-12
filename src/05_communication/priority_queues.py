import queue
import threading
import time


def do_work(item):
    print(f'{threading.current_thread()} removed {item} from the queue')


def worker(queue):
    while not queue.empty():
        item = queue.get()
        if item is None:
            print('item is none')
            break
        do_work(item)
        queue.task_done()
        time.sleep(1)


q = queue.PriorityQueue()

for i in range(5):
    q.put((i, i))

for i in range(5):
    q.put((i, i))

print('Queue populated')

threads = []
for i in range(2):
    thread = threading.Thread(target=worker, args=(q,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print('Queue is empty')

'''
Queue populated
<Thread(Thread-1, started 123145446420480)> removed (0, 0) from the queue
<Thread(Thread-2, started 123145463209984)> removed (0, 0) from the queue
<Thread(Thread-1, started 123145446420480)> removed (1, 1) from the queue
<Thread(Thread-2, started 123145463209984)> removed (1, 1) from the queue
<Thread(Thread-1, started 123145446420480)> removed (2, 2) from the queue
<Thread(Thread-2, started 123145463209984)> removed (2, 2) from the queue
<Thread(Thread-1, started 123145446420480)> removed (3, 3) from the queue
<Thread(Thread-2, started 123145463209984)> removed (3, 3) from the queue
<Thread(Thread-1, started 123145446420480)> removed (4, 4) from the queue
<Thread(Thread-2, started 123145463209984)> removed (4, 4) from the queue
Queue is empty
'''
