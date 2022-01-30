import threading
import time


def threadWorker():
    print('Running State')  # Runnable -> Running
    time.sleep(3)  # Running -> Not-running
    print('Terminating')


myThread = threading.Thread(target=threadWorker)  # New Thread
myThread.start()  # New Thread - start -> Runnable
myThread.join()

print('Dead')  # Runnable - run() end-> Dead
