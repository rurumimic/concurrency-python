import os
from multiprocessing import Pool


def task(x, y):
    print(f'{os.getpid()}: {(x, y)}')
    return y


def main():
    with Pool(processes=2, maxtasksperchild=2) as p:
        print(p.starmap_async(
            task, [(4, 3), (2, 1), (3, 2), (5, 1)]).get())
        print(p.starmap_async(
            task, [(4, 3), (2, 1), (3, 2), (5, 1), (6, 3)]).get())


if __name__ == '__main__':
    main()

'''
88500: (4, 3)
88500: (2, 1)
88499: (3, 2)
88499: (5, 1)
[3, 1, 2, 1]
88501: (4, 3)
88501: (2, 1)
88502: (3, 2)
88502: (5, 1)
88503: (6, 3)
[3, 1, 2, 1, 3]
'''
