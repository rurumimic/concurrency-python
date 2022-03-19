import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

values = [2, 3, 4, 5, 6, 7, 8]


def multiplyByTwo(n):
    print(f'Processing {n} in {threading.current_thread()}')
    return 2 * n


def main():
    print('Starting ThreadPoolExecutor')
    with ThreadPoolExecutor(max_workers=3) as executor:
        results = executor.map(multiplyByTwo, values)
    print([x for x in results])
    print('All tasks complete')


if __name__ == '__main__':
    main()
    results = list(map(multiplyByTwo, values))
    print(results)

'''
Starting ThreadPoolExecutor
Processing 2 in <Thread(ThreadPoolExecutor-0_0, started 123145572212736)>
Processing 3 in <Thread(ThreadPoolExecutor-0_0, started 123145572212736)>
Processing 4 in <Thread(ThreadPoolExecutor-0_2, started 123145605791744)>
Processing 5 in <Thread(ThreadPoolExecutor-0_0, started 123145572212736)>
Processing 7 in <Thread(ThreadPoolExecutor-0_2, started 123145605791744)>
Processing 6 in <Thread(ThreadPoolExecutor-0_1, started 123145589002240)>
Processing 8 in <Thread(ThreadPoolExecutor-0_0, started 123145572212736)>
[4, 6, 8, 10, 12, 14, 16]
All tasks complete

Processing 2 in <_MainThread(MainThread, started 4421772800)>
Processing 3 in <_MainThread(MainThread, started 4421772800)>
Processing 4 in <_MainThread(MainThread, started 4421772800)>
Processing 5 in <_MainThread(MainThread, started 4421772800)>
Processing 6 in <_MainThread(MainThread, started 4421772800)>
Processing 7 in <_MainThread(MainThread, started 4421772800)>
Processing 8 in <_MainThread(MainThread, started 4421772800)>
[4, 6, 8, 10, 12, 14, 16]
'''
