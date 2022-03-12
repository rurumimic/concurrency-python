import threading


def lock_class(funcs, lockfactory):
    return lambda cls: make_threadsafe(cls, funcs, lockfactory)


def lock_func(func):
    if getattr(func, '__is_locked', False):
        raise TypeError(f'Method {func!r} is already locked!')

    def locked_func(self, *args, **kwargs):
        with self._lock:
            return func(self, *args, **kwargs)
    locked_func.__name = f'lock_func({func.__name__})'
    locked_func.__is_locked = True
    return locked_func


def make_threadsafe(cls, funcs, lockfactory):
    init = cls.__init__

    def newinit(self, *arg, **kwarg):
        init(self, *arg, **kwarg)
        self._lock = lockfactory()
    cls.__init__ = newinit

    for func in funcs:
        oldfunc = getattr(cls, func)
        newfunc = lock_func(oldfunc)
        setattr(cls, func, newfunc)

    return cls


@lock_class(['add', 'remove'], threading.Lock)
class ClassDecoratorLockedSet(set):

    @lock_func  # if you double-lock a method, a TypeError is raised
    def lockedFunc(self):
        print('This section of our code would be thread safe')
        pass
