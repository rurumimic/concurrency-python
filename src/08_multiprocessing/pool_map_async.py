import time
from multiprocessing import Pool


def task(n):
    time.sleep(n/8)
    print(n)
    return n * 2


def main():
    with Pool(4) as p:
        print(p.map_async(task, [1, 2, 3, 4, 5, 6, 7, 8]).get())


if __name__ == '__main__':
    main()

'''
1 # sleep 1/8
2 # sleep 2/8
3 # sleep 3/8
4 # sleep 4/8
5 # sleep 5/8
6 # sleep 6/8
7 # sleep 7/8
8 # sleep 8/8
[2, 4, 6, 8, 10, 12, 14, 16]
'''
