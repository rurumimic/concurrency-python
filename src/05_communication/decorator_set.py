import threading
from functools import wraps


def lock(func):
    print('lock', func)

    @wraps(func)
    def wrapper(self, *args, **kwargs):
        with self._lock:
            return func(self, *args, **kwargs)
    return wrapper


class DecoratorLockedSet(set):
    def __init__(self, *args, **kwargs):
        self._lock = threading.Lock()
        super(DecoratorLockedSet, self).__init__(*args, **kwargs)

    @lock
    def add(self, e):
        return super(DecoratorLockedSet, self).add(e)

    @lock
    def remove(self, e):
        return super(DecoratorLockedSet, self).remove(e)
