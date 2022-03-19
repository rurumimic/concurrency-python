import multiprocessing
import time


def daemon_process():
    print(
        f'-- [{multiprocessing.current_process().name}]: {multiprocessing.current_process()}')
    print(f'PID: {multiprocessing.current_process().pid}')
    time.sleep(10)
    print('Daemon process terminating')


def main():
    print(
        f'-- [{multiprocessing.current_process().name}]: {multiprocessing.current_process()}')
    print(f'PID: {multiprocessing.current_process().pid}')
    process = multiprocessing.Process(
        target=daemon_process, name='Daemon Process')
    process.daemon = True
    process.start()

    print('We can carry on per usual and our daemon our will continue to execute')
    time.sleep(1)


if __name__ == '__main__':
    main()
    print('== END main() ==')

'''
-- [MainProcess]: <_MainProcess name='MainProcess' parent=None started>
PID: 74715
We can carry on per usual and our daemon our will continue to execute
-- [Daemon Process]: <Process name='Daemon Process' parent=74715 started daemon>
PID: 74726

# after 1 second
== END main() ==
'''
