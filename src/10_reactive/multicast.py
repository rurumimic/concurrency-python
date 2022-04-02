from random import randint

from rx import operators as op
from rx import range
from rx.core.typing import Observer


class Subscriber(Observer):

    def __init__(self, ident):
        self.id = ident

    def on_next(self, value):
        print(f'Subscriber: {self.id} Received: {value}')

    def on_completed(self):
        print(f'Subscriber: {self.id} Completed')

    def on_error(self, error):
        print(f'Error Occurred: {error}')


three_random_ints = range(1, 4).pipe(
    op.map(lambda i: randint(1, 100000)),
    op.publish()
)

three_random_ints.subscribe(Subscriber('Grant'))
three_random_ints.subscribe(Subscriber('Barry'))
three_random_ints.subscribe(Subscriber('Sophie'))
three_random_ints.connect()


'''
Subscriber: Grant Received: 69524
Subscriber: Barry Received: 69524
Subscriber: Sophie Received: 69524

Subscriber: Grant Received: 34358
Subscriber: Barry Received: 34358
Subscriber: Sophie Received: 34358

Subscriber: Grant Received: 14427
Subscriber: Barry Received: 14427
Subscriber: Sophie Received: 14427

Subscriber: Grant Completed
Subscriber: Barry Completed
Subscriber: Sophie Completed
'''
