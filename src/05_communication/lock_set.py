import threading


class LockSet(set):
    def __init__(self, *args, **kwagrs):
        self._lock = threading.Lock()
        super(LockSet, self).__init__(*args, **kwagrs)

    def add(self, e):
        with self._lock:
            super(LockSet, self).add(e)

    def remove(self, e):
        with self._lock:
            super(LockSet, self).remove(e)

    def __contains__(self, e):
        with self._lock:
            return super(LockSet, self).__contains__(e)
