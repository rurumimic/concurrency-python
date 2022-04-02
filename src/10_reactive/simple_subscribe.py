from rx import create
from rx.core.typing import Observer


def push_five_strings(observer, scheduler):
    observer.on_next('Alpha')
    observer.on_next('Beta')
    observer.on_next('Gamma')
    observer.on_next('Delta')
    observer.on_next('Epsilon')
    observer.on_completed()


class PrintObserver(Observer):
    def on_next(self, value):
        print(f'Received: {value}')

    def on_completed(self):
        print(f'Completed.')

    def on_error(self, error):
        print(f'Error: {error}')


source = create(push_five_strings)

source.subscribe(PrintObserver())
source.subscribe(
    on_next=lambda i: print(f'Received {i}'),
    on_error=lambda e: print(f'Error Occurred: {e}'),
    on_completed=lambda: print('Done!'),
)

'''
Received: Alpha
Received: Beta
Received: Gamma
Received: Delta
Received: Epsilon
Completed.
'''
