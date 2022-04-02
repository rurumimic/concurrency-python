import multiprocessing
import random
import time
from threading import current_thread

from rx import from_, interval
from rx import operators as op
from rx import range
from rx.scheduler import ThreadPoolScheduler


def processHeavyCalc(value):
    time.sleep(random.randint(5, 20) * .1)
    return value


# calculate number of CPU's, then create a ThreadPoolScheduler with that number of threads
optimal_thread_count = multiprocessing.cpu_count()
pool_scheduler = ThreadPoolScheduler(optimal_thread_count)

# Create Process 1
from_(['Alpha', 'Beta', 'Gamma', 'Delta', 'Epsilon']).pipe(
    op.map(lambda s: processHeavyCalc(s)),
    op.subscribe_on(pool_scheduler),
).subscribe(on_next=lambda s: print(f'PROCESS 1: {current_thread().name} {s}'),
            on_error=lambda e: print(e),
            on_completed=lambda: print('PROCESS 1 done!'))

# Create Process 2
range(1, 10).pipe(
    op.map(lambda s: processHeavyCalc(s)),
    op.subscribe_on(pool_scheduler),
).subscribe(on_next=lambda i: print(f'PROCESS 2: {current_thread().name} {i}'),
            on_error=lambda e: print(e), on_completed=lambda: print('PROCESS 2 done!'))

# Create Process 3, which is infinite
interval(1).pipe(
    op.map(lambda i: i * 100),
    op.observe_on(pool_scheduler),
    op.map(lambda s: processHeavyCalc(s)),
).subscribe(on_next=lambda i: print(f'PROCESS 3: {current_thread().name} {i}'),
            on_error=lambda e: print(e))

input('Press any key to exit\n')

'''
Press any key to exit
PROCESS 1: ThreadPoolExecutor-0_0 Alpha
PROCESS 1: ThreadPoolExecutor-0_0 Beta
PROCESS 2: ThreadPoolExecutor-0_1 1
PROCESS 3: ThreadPoolExecutor-0_2 0
PROCESS 2: ThreadPoolExecutor-0_1 2
PROCESS 3: ThreadPoolExecutor-0_3 100
PROCESS 1: ThreadPoolExecutor-0_0 Gamma
PROCESS 2: ThreadPoolExecutor-0_1 3
PROCESS 2: ThreadPoolExecutor-0_1 4
PROCESS 3: ThreadPoolExecutor-0_3 200
PROCESS 1: ThreadPoolExecutor-0_0 Delta
PROCESS 3: ThreadPoolExecutor-0_3 300
PROCESS 2: ThreadPoolExecutor-0_1 5
PROCESS 1: ThreadPoolExecutor-0_0 Epsilon
PROCESS 1 done!
PROCESS 3: ThreadPoolExecutor-0_3 400
PROCESS 2: ThreadPoolExecutor-0_1 6
PROCESS 3: ThreadPoolExecutor-0_3 500
PROCESS 3: ThreadPoolExecutor-0_3 600
PROCESS 2: ThreadPoolExecutor-0_1 7
PROCESS 2: ThreadPoolExecutor-0_1 8
PROCESS 3: ThreadPoolExecutor-0_3 700
PROCESS 2: ThreadPoolExecutor-0_1 9
PROCESS 2 done!
PROCESS 3: ThreadPoolExecutor-0_3 800
PROCESS 3: ThreadPoolExecutor-0_3 900
PROCESS 3: ThreadPoolExecutor-0_3 1000
PROCESS 3: ThreadPoolExecutor-0_3 1100
PROCESS 3: ThreadPoolExecutor-0_3 1200
PROCESS 3: ThreadPoolExecutor-0_3 1300
PROCESS 3: ThreadPoolExecutor-0_3 1400
PROCESS 3: ThreadPoolExecutor-0_3 1500
...
'''
