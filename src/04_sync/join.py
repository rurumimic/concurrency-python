import threading
import time


def ourThread(i):
    print(f'Thread {i} started')
    time.sleep(i * 2)
    print(f'Thread {i} finished')


def main():
    thread1 = threading.Thread(target=ourThread, args=(1,))
    thread1.start()
    print('Is thread 1 finished?')
    thread2 = threading.Thread(target=ourThread, args=(2,))
    thread2.start()
    thread2.join()
    print('Thread 2 definitely finished')


if __name__ == '__main__':
    main()

'''
Thread 1 started
Is thread 1 finished?
Thread 2 started
Thread 1 finished
Thread 2 finished
Thread 2 definitely finished
'''
