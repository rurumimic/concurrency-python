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


q = queue.LifoQueue()
for i in range(10):
    q.put(i)


print('Queue populated')

threads = []
for i in range(4):
    thread = threading.Thread(target=worker, args=(q,))
    thread.start()
    threads.append(thread)

# block until all tasks are done
# q.join()
#
# stop workers
# for i in range(4):
#     q.put(None)

for thread in threads:
    thread.join()

print('Queue is empty')

'''
Queue populated
<Thread(Thread-1, started 123145550643200)> removed 9 from the queue
<Thread(Thread-2, started 123145567432704)> removed 8 from the queue
<Thread(Thread-3, started 123145584222208)> removed 7 from the queue
<Thread(Thread-4, started 123145601011712)> removed 6 from the queue
<Thread(Thread-1, started 123145550643200)> removed 5 from the queue
<Thread(Thread-2, started 123145567432704)> removed 4 from the queue
<Thread(Thread-4, started 123145601011712)> removed 3 from the queue
<Thread(Thread-3, started 123145584222208)> removed 2 from the queue
<Thread(Thread-1, started 123145550643200)> removed 1 from the queue
<Thread(Thread-2, started 123145567432704)> removed 0 from the queue
Queue is empty
'''
