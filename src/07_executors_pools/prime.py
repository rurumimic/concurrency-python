import math
import timeit
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

PRIMES = [
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    112272535095293,
    112582705942171,
    112272535095293,
    1099726899285419
]


def is_prime(n):
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))

    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


def main():
    t1 = timeit.default_timer()
    with ProcessPoolExecutor(max_workers=4) as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print(f'{number} is prime: {prime}')

    print(f'{timeit.default_timer() - t1} Seconds Needed for ProcessPoolExecutor')

    t2 = timeit.default_timer()
    with ThreadPoolExecutor(max_workers=4) as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print(f'{number} is prime: {prime}')

    print(f'{timeit.default_timer() - t2} Seconds Needed for ThreadPoolExecutor')

    t3 = timeit.default_timer()
    for number in PRIMES:
        prime = is_prime(number)
        print(f'{number} is prime: {prime}')
    print(f'{timeit.default_timer() - t3} Seconds Needed for single threaded')


if __name__ == '__main__':
    main()

'''
0.736759732 Seconds Needed for ProcessPoolExecutor
1.8963157449999999 Seconds Needed for ThreadPoolExecutor
1.8906895159999997 Seconds Needed for single threaded
'''
