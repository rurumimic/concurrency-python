import time
from multiprocessing import Pool


def task(n):
    time.sleep(n/2)
    return n * 2


def main():
    with Pool(4) as p:
        print(p.apply(task, (4, )))  # == ThreadPoolExecutor.submit()
        print(p.apply(task, (3, )))
        print(p.apply(task, (2, )))
        print(p.apply(task, (1, )))


if __name__ == '__main__':
    main()

'''
# sleep 2
8
# sleep 1.5
6
# sleep 1
4
# sleep 0.5
2
'''
