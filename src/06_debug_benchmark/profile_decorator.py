import random
import time


@profile
def slowFunction():
    time.sleep(random.randint(1, 3))
    print('Slow Function Executed')


def fastFunction():
    print('Fast Function Executed')


def main():
    slowFunction()
    fastFunction()


if __name__ == '__main__':
    main()
