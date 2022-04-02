from rx import interval
from rx import operators as op

interval(1).pipe(
    op.map(lambda i: f'{i} Mississippi')
).subscribe(lambda s: print(s))

input("Press any key to quit\n")

'''
Press any key to quit
0 Mississippi
1 Mississippi
2 Mississippi
3 Mississippi
4 Mississippi
5 Mississippi
'''
