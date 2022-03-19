import logging
from multiprocessing import Pool

logging.basicConfig(filename='myapp.log', level=logging.INFO,
                    format='%(processName)-10s:%(asctime)s:%(levelname)s:%(message)s')


def task(n):
    logging.info(f'{n} being processed')
    logging.info(f'Final Result: {n * 2}')
    return n * 2


def main():
    with Pool(4) as p:
        p.map(task, [2, 3, 4, 5, 6, ])


if __name__ == '__main__':
    main()

'''
SpawnPoolWorker-3:2022-03-19 16:31:26,788:INFO:2 being processed
SpawnPoolWorker-3:2022-03-19 16:31:26,788:INFO:Final Result: 4
SpawnPoolWorker-3:2022-03-19 16:31:26,788:INFO:3 being processed
SpawnPoolWorker-3:2022-03-19 16:31:26,788:INFO:Final Result: 6
SpawnPoolWorker-3:2022-03-19 16:31:26,788:INFO:4 being processed
SpawnPoolWorker-3:2022-03-19 16:31:26,788:INFO:Final Result: 8
SpawnPoolWorker-3:2022-03-19 16:31:26,788:INFO:5 being processed
SpawnPoolWorker-3:2022-03-19 16:31:26,788:INFO:Final Result: 10
SpawnPoolWorker-3:2022-03-19 16:31:26,788:INFO:6 being processed
SpawnPoolWorker-3:2022-03-19 16:31:26,789:INFO:Final Result: 12
'''
