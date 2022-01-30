import os


def child():
    print(f'Child PID {os.getpid()}')


def parent():
    print(f'Parent PID {os.getpid()}')

    newRef = os.fork()

    if newRef == 0:
        child()
    else:
        print(f'Parent has {newRef}')


parent()

'''
Parent PID 73033
Parent has 73035
Child PID 73035
'''
