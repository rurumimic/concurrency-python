import threading
import time
import random


def myThread(i):
    print(f'Thread {i} started')
    time.sleep(random.randint(1, 5))
    print(f'Thread {i} finished')


def main():
    for i in range(random.randint(2, 50)):
        thread = threading.Thread(target=myThread, args=(i,))
        thread.start()
    time.sleep(4)
    # main thread 1 + myThread 14 = 15
    print(f'Total Number of Active Threads: {threading.active_count()}')


if __name__ == '__main__':
    main()

'''
...

Total Number of Active Threads: 15
Thread 0 finished
Thread 3 finished
Thread 1 finished
Thread 4 finished
Thread 14 finished
Thread 17 finished
Thread 21 finished
Thread 25 finished
Thread 38 finished
Thread 34 finished
Thread 31 finished
Thread 43 finished
Thread 29 finished
Thread 41 finished
'''
