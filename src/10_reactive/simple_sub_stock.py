from rx import create
from rx.core.typing import Observer

stocks = [
    {'TCKR': 'APPL', 'PRICE': 200},  # > 100
    {'TCKR': 'GOOG', 'PRICE': 90},
    {'TCKR': 'TSLA', 'PRICE': 120},  # > 100
    {'TCKR': 'MSFT', 'PRICE': 150},  # > 100
    {'TCKR': 'INTL', 'PRICE': 70},
]


def buy_stock_events(observer, scheduler):
    for stock in stocks:
        if(stock['PRICE'] > 100):
            observer.on_next(stock['TCKR'])
    observer.on_completed()


class StockObserver(Observer):

    def on_next(self, value):
        print(f'Received Instruction to buy {value}')

    def on_completed(self):
        print('All Buy Instructions have been received')

    def on_error(self, error):
        print(f'Error Occurred: {error}')


source = create(buy_stock_events)
source.subscribe(StockObserver())

'''
Received Instruction to buy APPL
Received Instruction to buy TSLA
Received Instruction to buy MSFT
All Buy Instructions have been received
'''
