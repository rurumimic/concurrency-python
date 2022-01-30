import threading
import time


def threadTarget():
    print(f'Current: {threading.current_thread()}')


threads = []

for i in range(10):
    thread = threading.Thread(target=threadTarget)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

'''
Current: <Thread(Thread-1 (threadTarget), started 123145513545728)>
Current: <Thread(Thread-2 (threadTarget), started 123145530335232)>
Current: <Thread(Thread-3 (threadTarget), started 123145513545728)>
Current: <Thread(Thread-4 (threadTarget), started 123145530335232)>
Current: <Thread(Thread-5 (threadTarget), started 123145513545728)>
Current: <Thread(Thread-6 (threadTarget), started 123145530335232)>
Current: <Thread(Thread-7 (threadTarget), started 123145513545728)>
Current: <Thread(Thread-8 (threadTarget), started 123145530335232)>
Current: <Thread(Thread-9 (threadTarget), started 123145513545728)>
Current: <Thread(Thread-10 (threadTarget), started 123145513545728)>
'''
