import random
import threading
import time


class myThread(threading.Thread):
    def __init__(self, barrier):
        threading.Thread.__init__(self)
        self.barrier = barrier

    def run(self):
        print(f'Thread {threading.current_thread()} working')
        time.sleep(random.randint(1, 10))
        print(
            f'Thread {threading.current_thread()} is joining {self.barrier.n_waiting} waiting on barrier')

        self.barrier.wait()
        print('Barrier has been lifted, continuing with work')


barrier = threading.Barrier(4)
threads = []


for i in range(4):
    thread = myThread(barrier)
    thread.start()
    threads.append(thread)
for t in threads:
    t.join()

'''
Thread <myThread(Thread-1, started 123145490481152)> working
Thread <myThread(Thread-2, started 123145507270656)> working
Thread <myThread(Thread-3, started 123145524060160)> working
Thread <myThread(Thread-4, started 123145540849664)> working
Thread <myThread(Thread-1, started 123145490481152)> is joining 0 waiting on barrier
Thread <myThread(Thread-3, started 123145524060160)> is joining 1 waiting on barrier
Thread <myThread(Thread-4, started 123145540849664)> is joining 2 waiting on barrier
Thread <myThread(Thread-2, started 123145507270656)> is joining 3 waiting on barrier
Barrier has been lifted, continuing with work
Barrier has been lifted, continuing with work
Barrier has been lifted, continuing with work
Barrier has been lifted, continuing with work
'''
