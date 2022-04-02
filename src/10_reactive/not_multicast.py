from random import randint

from rx import operators as op
from rx import range

three_random_ints = range(1, 4).pipe(
    op.map(lambda i: randint(1, 100000))
)

three_random_ints.subscribe(lambda i: print(f'Subscriber 1 Received: {i}'))
three_random_ints.subscribe(lambda i: print(f'Subscriber 2 Received: {i}'))

'''
Subscriber 1 Received: 12440
Subscriber 1 Received: 57115
Subscriber 1 Received: 53049

Subscriber 2 Received: 69131
Subscriber 2 Received: 95827
Subscriber 2 Received: 19671
'''
