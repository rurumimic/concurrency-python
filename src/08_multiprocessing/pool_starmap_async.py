import time
from multiprocessing import Pool


def task(x, y):
    time.sleep(x/2)
    print((x, y))
    return y


def main():
    with Pool(4) as p:
        print(p.starmap_async(task, [(4, 3), (2, 1)]).get())


if __name__ == '__main__':
    main()

'''
(2, 1)
(4, 3)

[3, 1]
'''
