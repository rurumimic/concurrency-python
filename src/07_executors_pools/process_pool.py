import os
import time
from concurrent.futures import ProcessPoolExecutor


def task(n):
    time.sleep(1)
    print(f'Executing our Task {n} on Process {os.getpid()}')


def main():
    with ProcessPoolExecutor(max_workers=3) as executor:
        task1 = executor.submit(task, (1))
        task2 = executor.submit(task, (2))


if __name__ == '__main__':
    main()

'''
Executing our Task 2 on Process 93766
Executing our Task 1 on Process 93765
'''
