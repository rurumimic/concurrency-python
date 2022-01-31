import threading


class SafeSet(set):
    def __init__(self, *args, **kwagrs):
        self._lock = threading.Lock()
        super(SafeSet, self).__init__(*args, **kwagrs)

    def add(self, e):
        with self._lock:
            super(SafeSet, self).add(e)

    def remove(self, e):
        with self._lock:
            super(SafeSet, self).remove(e)

    def __contains__(self, e):
        with self._lock:
            return super(SafeSet, self).__contains__(e)
