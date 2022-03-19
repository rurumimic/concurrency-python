import threading
import time
from concurrent.futures import ThreadPoolExecutor


def task(n):
    time.sleep(1)
    print(f'Processing {n} in {threading.current_thread()}')


def main():
    print('Starting ThreadPoolExecutor')
    with ThreadPoolExecutor(max_workers=3) as executor:
        future = executor.submit(task, (2))
        future = executor.submit(task, (3))
        future = executor.submit(task, (4))
    print('All tasks complete')


if __name__ == '__main__':
    main()

'''
Starting ThreadPoolExecutor
Processing 2 in <Thread(ThreadPoolExecutor-0_0, started 123145379749888)>
Processing 3 in <Thread(ThreadPoolExecutor-0_1, started 123145396539392)>
Processing 4 in <Thread(ThreadPoolExecutor-0_2, started 123145413328896)>
All tasks complete
'''
