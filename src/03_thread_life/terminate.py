from multiprocessing import Process
import time


def myWorker():
    t1 = time.time()
    print(f'Process started at: {t1}')
    time.sleep(5)


myProcess = Process(target=myWorker)
print(f'Process {myProcess}')
myProcess.start()
print('Terminating Process...')
myProcess.terminate()
myProcess.join()
print(f'Process Terminated: {myProcess}')

'''
Process <Process name='Process-1' parent=84197 initial>
Terminating Process...
Process Terminated: <Process name='Process-1' pid=84207 parent=84197 stopped exitcode=-SIGTERM>
'''
