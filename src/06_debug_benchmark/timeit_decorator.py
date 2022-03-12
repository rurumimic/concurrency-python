import random
import time
import timeit


def timethis(func):

    def function_timer(*args, **kwargs):
        start_time = timeit.default_timer()
        value = func(*args, **kwargs)
        runtime = timeit.default_timer() - start_time
        print(f'Function {func.__name__} took {runtime} seconds to run')
        return value
    return function_timer


@timethis
def long_runner():
    for _ in range(3):
        sleep_time = random.choice(range(1, 3))
        time.sleep(sleep_time)


if __name__ == '__main__':
    long_runner()

'''
Function long_runner took 6.010552367 seconds to run
'''
