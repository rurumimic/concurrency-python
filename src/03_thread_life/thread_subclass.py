import threading
from threading import Thread


class myWorkerThread(Thread):

    def __init__(self):
        print('Hello world')  # 1
        Thread.__init__(self)

    def run(self):
        print(f'Thread is now running: {threading.current_thread()}')  # 3.2


myThread = myWorkerThread()  # 0
print('Created my Thread Object')  # 2
myThread.start()  # 3.1
print('Started my thread')  # 4
myThread.join()
print('My Thread finished')  # 5
myThread.run()  # == Main

'''
Hello world
Created my Thread Object
Thread is now running: <myWorkerThread(Thread-1, started 123145343193088)>
Started my thread
My Thread finished
Thread is now running: <_MainThread(MainThread, started 4507997696)>
'''
