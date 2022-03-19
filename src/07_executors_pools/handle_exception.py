from concurrent.futures import ThreadPoolExecutor, as_completed


def is_even(n):
    print(f'Checking if {n} is even')
    if type(n) != int:
        raise Exception('Value entered is not an integer')
    if n % 2 == 0:
        print(f'{n} is even')
        return True
    else:
        print(f'{n} is odd')
        return False


def handler(fn):
    if fn.cancelled():
        print(f'[handler] Our {fn.arg} Future has been cancelled')
        return
    if fn.done():
        print(f'[handler] Our Task has completed')

        for future in as_completed([fn]):
            try:
                print(f'[handler] {future.result()}')
            except Exception as e:
                print(f'[handler] [Exception] {e}')


def main():
    with ThreadPoolExecutor(max_workers=4) as executor:
        task1 = executor.submit(is_even, (2))
        task2 = executor.submit(is_even, (3))
        task3 = executor.submit(is_even, ('t'))

        task3.add_done_callback(handler)

    for future in as_completed([task1, task2, task3]):
        try:
            print(f'Result of Task: {future.result()}')
        except Exception as e:
            print(f'[Exception] {e}')


if __name__ == '__main__':
    main()

'''
Checking if 2 is even
2 is even

Checking if 3 is even
3 is odd

Checking if t is even
[handler] Our Task has completed
[handler] [Exception] Value entered is not an integer

Result of Task: True
[Exception] Value entered is not an integer
Result of Task: False
'''
