from threading import Thread


class myWorkerThread(Thread):

    def __init__(self):
        print('Hello world')  # 1
        Thread.__init__(self)

    def run(self):
        print('Thread is now running')  # 3.2


myThread = myWorkerThread()  # 0
print('Created my Thread Object')  # 2
myThread.start()  # 3.1
print('Started my thread')  # 4
myThread.join()
print('My Thread finished')  # 5
