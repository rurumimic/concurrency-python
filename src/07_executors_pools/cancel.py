import random
import time
from concurrent.futures import ThreadPoolExecutor


def task(n):
    print(f'Executing Task {n}')
    time.sleep(n)
    print(f'Task {n} Finished Executing')


def main():
    with ThreadPoolExecutor(max_workers=2) as executor:
        task1 = executor.submit(task, (1))
        task2 = executor.submit(task, (2))
        task3 = executor.submit(task, (3))
        task4 = executor.submit(task, (4))

        print(task3.cancel())  # True / False


if __name__ == '__main__':
    main()

'''
Executing Task 1
Executing Task 2
True
Task 1 Finished Executing
Executing Task 4
Task 2 Finished Executing
Task 4 Finished Executing
'''

'''
Executing Task 1
Task 1 Finished Executing
Executing Task 2
Task 2 Finished Executing
Executing Task 3
Task 3 Finished Executing
False
Executing Task 4
Task 4 Finished Executing
'''
