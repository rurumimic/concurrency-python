from asyncio import sleep
import threading
import time
import random


def executeThread(i):
    print(f'Thread {i} started')
    sleepTime = random.randint(1, 10)
    time.sleep(sleepTime)
    print(f'Thread {i} finished executing')


for i in range(10):
    thread = threading.Thread(target=executeThread, args=(i,))
    thread.start()
    print('Active Threads:', threading.enumerate())

'''
Thread 0 started
Active Threads: [<_MainThread(MainThread, started 4681729472)>, <Thread(Thread-1 (executeThread), started 123145515708416)>]
Thread 1 started
...

Thread 9 started
Active Threads: [<_MainThread(MainThread, started 4681729472)>, <Thread(Thread-1 (executeThread), started 123145515708416)>, <Thread(Thread-2 (executeThread), started 123145532497920)>, <Thread(Thread-3 (executeThread), started 123145549287424)>, <Thread(Thread-4 (executeThread), started 123145566076928)>, <Thread(Thread-5 (executeThread), started 123145582866432)>, <Thread(Thread-6 (executeThread), started 123145599655936)>, <Thread(Thread-7 (executeThread), started 123145616445440)>, <Thread(Thread-8 (executeThread), started 123145633234944)>, <Thread(Thread-9 (executeThread), started 123145650024448)>, <Thread(Thread-10 (executeThread), started 123145666813952)>]
Thread 3 finished executing
Thread 4 finished executing
Thread 9 finished executing
Thread 2 finished executing
Thread 5 finished executing
Thread 7 finished executing
Thread 6 finished executing
Thread 0 finished executing
Thread 1 finished executing
Thread 8 finished executing
'''
