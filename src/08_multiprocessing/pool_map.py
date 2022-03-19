import time
from multiprocessing import Pool


def task(n):
    time.sleep(1)
    print(n)
    return n * 3


def main():
    with Pool(4) as p:
        print(p.map(task, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))


if __name__ == '__main__':
    main()

'''
# sleep 1

1
2
3
4

# sleep 1

5
6
7
8

# sleep 1

9
10
11

[3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33]
'''
