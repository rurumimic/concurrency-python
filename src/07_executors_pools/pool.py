import threading
import time
from concurrent.futures import ThreadPoolExecutor


def task():
    time.sleep(1)

    print('Executing our Task')
    result = 0
    for i in range(10):
        result = result + i
    print(f'I: {result}')
    print(f'Task Executed {threading.current_thread()}')


def main():
    executor = ThreadPoolExecutor(max_workers=3)
    task1 = executor.submit(task)
    task2 = executor.submit(task)


if __name__ == '__main__':
    main()

'''
Executing our Task
I: 45
Executing our Task
I: 45
Task Executed <Thread(ThreadPoolExecutor-0_0, started 123145405440000)>
Task Executed <Thread(ThreadPoolExecutor-0_1, started 123145422229504)>
'''
