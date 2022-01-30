import threading
import time


def myThread():
    print(f'Thread {threading.current_thread().name} started')
    time.sleep(5)
    print(f'Thread {threading.current_thread().name} finished')


for i in range(4):
    threadName = 'Thread-' + str(i)
    thread = threading.Thread(name=threadName, target=myThread)
    thread.start()

print(f'{threading.enumerate()}')

'''
Thread Thread-0 started
Thread Thread-1 started
Thread Thread-2 started
Thread Thread-3 started
[
  <_MainThread(MainThread, started 4593550784)>, 
  <Thread(Thread-0, started 123145357635584)>, 
  <Thread(Thread-1, started 123145374425088)>, 
  <Thread(Thread-2, started 123145391214592)>, 
  <Thread(Thread-3, started 123145408004096)>
]
Thread Thread-0 finished
Thread Thread-1 finished
Thread Thread-3 finished
Thread Thread-2 finished
'''
