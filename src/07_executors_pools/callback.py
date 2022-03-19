from concurrent.futures import ThreadPoolExecutor


def task(n):
    print(f'Processing {n}')


def task_done(fn):
    if fn.cancelled():
        print(f'Our {fn.arg} Future has been cancelled')
    elif fn.done():
        print('Our Task has completed')


def second_task_done(fn):
    print('I didn\'t think this would work')


def main():
    print('Starting ThreadPoolExecutor')
    with ThreadPoolExecutor(max_workers=3) as executor:
        future = executor.submit(task, (2))
        future.add_done_callback(task_done)
        future.add_done_callback(second_task_done)

    print('All tasks complete')


if __name__ == '__main__':
    main()

'''
Starting ThreadPoolExecutor
Processing 2
Our Task has completed
I didn't think this would work
All tasks complete
'''
