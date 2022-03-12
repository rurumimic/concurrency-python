import time
import timeit


def func1():
    print('Function 1 Executing')
    time.sleep(1)
    print('Function 1 complete')
    print('---')


def func2():
    print('Function 2 executing')
    time.sleep(2)
    print('Function 2 complete')
    print('---')


t1 = timeit.Timer('func1()', setup='from __main__ import func1')
times = t1.repeat(repeat=2, number=1)
for t in times:
    print(f'{t} Seconds')

print('===============')

t2 = timeit.Timer('func2()', setup='from __main__ import func2')
times = t2.repeat(repeat=2, number=1)
for t in times:
    print(f'{t} Seconds')

'''
Function 1 Executing
Function 1 complete
---
Function 1 Executing
Function 1 complete
---
1.005327334 Seconds
1.005288055 Seconds
===============
Function 2 executing
Function 2 complete
---
Function 2 executing
Function 2 complete
---
2.004583729 Seconds
2.003876064 Seconds
'''
