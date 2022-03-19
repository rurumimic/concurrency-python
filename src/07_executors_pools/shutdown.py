import time
from concurrent.futures import ThreadPoolExecutor


def task(n):
    print(f'Executing Task {n}')
    time.sleep(n)
    print(f'Task {n} Finished Executing')


def main():
    with ThreadPoolExecutor(max_workers=2) as executor:
        task1 = executor.submit(task, (1))  # Executing Task 1
        task2 = executor.submit(task, (2))  # Executing Task 2

        print(executor.shutdown(wait=False))

        # Task 1 Finished Executing
        # Task 2 Finished Executing

        # RuntimeError: cannot schedule new futures after shutdown
        # task3 = executor.submit(task, (3))
        # task4 = executor.submit(task, (4))


if __name__ == '__main__':
    main()

'''
print(executor.shutdown(wait=False))

Executing Task 1
Executing Task 2
None
Task 1 Finished Executing
Task 2 Finished Executing
'''

'''
print(executor.shutdown(wait=True))

Executing Task 1
Executing Task 2
Task 1 Finished Executing
Task 2 Finished Executing
None
'''
