import os
import time
from multiprocessing import Pool


def task(n):
    print(f'Task by PID: {os.getpid()}')
    time.sleep(1)
    return n * 2


def main():
    with Pool(4) as p:
        tasks = []
        for i in range(4):
            t = p.apply_async(func=task, args=(i, ))
            tasks.append(t)

        for t in tasks:
            t.wait()
            print(f'Result: {t.get()}')


if __name__ == '__main__':
    main()

'''
Task by PID: 79805
Task by PID: 79805
Task by PID: 79805
Task by PID: 79805
Result: 0
Result: 2
Result: 4
Result: 6
'''
