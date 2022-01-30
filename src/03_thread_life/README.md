# Thread Life

John Bell: [Multithreading Models](https://www2.cs.uic.edu/~jbell/CourseNotes/OperatingSystems/4_Threads.html)

---

1. New Thread
2. Start -> Runnable
3. Running
4. Not Running
5. Dead

```py
t = threading.Thread(target=func, args=(i,))
t.start()
# t.join(timeout=%f) # wait until the thread terminates or timeout
```

## Thread()

python/cpython: [class Thread](https://github.com/python/cpython/blob/8b1b27f1939cc4060531d198fdb09242f247ca7c/Lib/threading.py#L831)

```py
def __init__(
  self,
  group=None, # ThreadGroup
  target=None, # callable object to be invoked by the run()
  name=None, # thread name. By default, a unique name "Thread-%d ({target.__name__})"
  args=(), # argument tuple ()
  kwargs=None, # dictionary of keyword arguments {}
  *,
  daemon=None # daemon threads are abruptly stopped at shutdown.
):
```

### Subclass

python/cpython: [Thread.\_\_init\_\_(self)](https://github.com/python/cpython/blob/8b1b27f1939cc4060531d198fdb09242f247ca7c/Lib/threading.py#L860-L862)

### Process fork

```py
import os

os.fork()
os.getpid()
```

### Daemon thread

ex: Heartbeat Signal

```py
myThread.daemon = True
```

### Terminate

```py
from multiprocessing import Process

myProcess = Process(target=myWorker)
myProcess.start()
myProcess.terminate()
myProcess.join()
```
