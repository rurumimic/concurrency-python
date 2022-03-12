import queue
import threading
import time


def do_work(item):
    print(f'{threading.current_thread()} removed {item} from the queue')


def worker(queue):
    time.sleep(1)
    while not queue.empty():
        item = queue.get()
        if item is None:
            print('item is none')
            break
        do_work(item)
        queue.task_done()


q = queue.Queue()
for i in range(5):
    q.put(i)

print('Queue populated')

# thread = threading.Thread(target=worker, args=(q,))
# thread.start()

print('Not Progressing Till Queue is Empty')

# fake task_done
q.task_done()
q.task_done()
q.task_done()
q.task_done()
q.task_done()

# block until all tasks are done
q.join()

print('Queue is now empty')
