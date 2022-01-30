import threading
import time


def myChildThread():
    print('Child Thread Starting')
    time.sleep(5)
    print('Current Thread ------')
    print(threading.current_thread())
    print('---------------------')
    print('Main Thread ---------')
    print(threading.main_thread())
    print('---------------------')
    print('Child Thread Ending')


child = threading.Thread(target=myChildThread)
child.start()
child.join()

'''
Child Thread Starting
Current Thread ------
<Thread(Thread-1 (myChildThread), started 123145577377792)>
---------------------
Main Thread ---------
<_MainThread(MainThread, started 4534658496)>
---------------------
Child Thread Ending
'''
