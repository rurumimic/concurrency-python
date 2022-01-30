# Sync

## Reentrant-lock, RLocks

**Same thread** can acquire **multiple times**.

```py
import threading

rlock = threading.RLock()
print(rlock)
with rlock:
    print(rlock)
    with rlock:
        print(rlock)
        with rlock:
            print(rlock)
        print(rlock)
    print(rlock)
print(rlock)
```

```bash
<unlocked _thread.RLock object owner=0 count=0 at 0x104a68080>
<locked _thread.RLock object owner=4411745728 count=1 at 0x104a68080>
<locked _thread.RLock object owner=4411745728 count=2 at 0x104a68080>
<locked _thread.RLock object owner=4411745728 count=3 at 0x104a68080>
<locked _thread.RLock object owner=4411745728 count=2 at 0x104a68080>
<locked _thread.RLock object owner=4411745728 count=1 at 0x104a68080>
<unlocked _thread.RLock object owner=0 count=0 at 0x104a68080>
```

## Condition

python/cpython: [class Condition](https://github.com/python/cpython/blob/8b1b27f1939cc4060531d198fdb09242f247ca7c/Lib/threading.py#L224)

```py
def __init__(self, lock=None):
    if lock is None:
        lock = RLock()
    # ...
```

## Semaphore

python/cpython: [class Semaphore](https://github.com/python/cpython/blob/8b1b27f1939cc4060531d198fdb09242f247ca7c/Lib/threading.py#L403)

```py
def __init__(self, value=1):
    if value < 0:
        raise ValueError("semaphore initial value must be >= 0")
    self._cond = Condition(Lock())
    self._value = value
```
