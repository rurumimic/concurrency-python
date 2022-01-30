import threading
import time
import random


def myThread(i):
    print(f'Thread {i} started')
    time.sleep(random.randint(1, 5))
    print(f'Thread {i} finished')


def main():
    for i in range(4):
        thread = threading.Thread(target=myThread, args=(i,))
        thread.start()
    print(f'Enumerating: {threading.enumerate()}')


if __name__ == '__main__':
    main()

'''
Thread 0 started
Thread 1 started
Thread 2 started
Thread 3 started
Enumerating: [
  <_MainThread(MainThread, started 4530197952)>, 
  <Thread(Thread-1 (myThread), started 123145525501952)>, 
  <Thread(Thread-2 (myThread), started 123145542291456)>, 
  <Thread(Thread-3 (myThread), started 123145559080960)>, 
  <Thread(Thread-4 (myThread), started 123145575870464)>
]
Thread 1 finished
Thread 2 finished
Thread 0 finished
Thread 3 finished
'''
