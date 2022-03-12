import random
import threading
import time


def worker():
    for _ in range(5):
        print('Starting wait time')
        time.sleep(random.randint(1, 3))
        print('Completed Wait')


threads = []
for i in range(3):
    thread = threading.Thread(target=worker)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

'''
python -m cProfile benchmark.py

Starting wait time
...
Completed Wait
         1779 function calls (1751 primitive calls) in 10.016 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      7/2    0.000    0.000    0.004    0.002 <frozen importlib._bootstrap>:1002(_find_and_load)
        7    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:112(release)
        7    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:152(__init__)
        7    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:156(__enter__)
        7    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:160(__exit__)
        7    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:166(_get_module_lock)
        7    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:185(cb)
     11/2    0.000    0.000    0.003    0.001 <frozen importlib._bootstrap>:220(_call_with_frames_removed)
      127    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:231(_verbose_message)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:35(_new_module)
        7    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:351(__init__)
       10    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:385(cached)
        7    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:398(parent)
        7    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:406(has_location)
        7    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:486(_init_module_attrs)
        7    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap>:558(module_from_spec)
        7    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:58(__init__)
      7/2    0.000    0.000    0.003    0.002 <frozen importlib._bootstrap>:659(_load_unlocked)
        7    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:736(find_spec)
        7    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:811(find_spec)
        7    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:87(acquire)
       21    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:874(__enter__)
       21    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:878(__exit__)
        7    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap>:901(_find_spec)
      7/2    0.000    0.000    0.004    0.002 <frozen importlib._bootstrap>:967(_find_and_load_unlocked)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1017(path_stats)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1095(__init__)
        4    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:1106(create_module)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1114(exec_module)
       32    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1272(_path_importer_cache)
        7    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:1309(_get_spec)
        7    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:1341(find_spec)
        7    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1433(_get_spec)
       25    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:1438(find_spec)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:301(cache_from_source)
       25    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:36(_relax_case)
        7    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:431(_get_cached)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:463(_check_name_wrapper)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:500(_classify_pyc)
        9    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:51(_unpack_uint32)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:533(_validate_timestamp_pyc)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:585(_compile_bytecode)
      112    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:62(_path_join)
        7    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:636(spec_from_file_location)
      112    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:64(<listcomp>)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:68(_path_split)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:781(create_module)
      3/2    0.000    0.000    0.003    0.002 <frozen importlib._bootstrap_external>:784(exec_module)
       35    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:80(_path_stat)
        3    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:856(get_code)
        7    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:90(_path_is_mode_type)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:946(__init__)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:971(get_filename)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:976(get_data)
        7    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:99(_path_isfile)
        1    0.000    0.000    0.000    0.000 _weakrefset.py:37(__init__)
        4    0.000    0.000    0.000    0.000 _weakrefset.py:82(add)
        1    0.000    0.000   10.016   10.016 benchmark.py:1(<module>)
        1    0.000    0.000    0.000    0.000 bisect.py:1(<module>)
        1    0.000    0.000    0.003    0.003 random.py:1(<module>)
        1    0.000    0.000    0.000    0.000 random.py:100(Random)
        1    0.000    0.000    0.000    0.000 random.py:116(__init__)
        1    0.000    0.000    0.000    0.000 random.py:125(seed)
        1    0.000    0.000    0.000    0.000 random.py:217(__init_subclass__)
        1    0.000    0.000    0.000    0.000 random.py:770(SystemRandom)
        1    0.000    0.000    0.000    0.000 threading.py:1(<module>)
        3    0.000    0.000   10.011    3.337 threading.py:1035(_wait_for_tstate_lock)
        7    0.000    0.000    0.000    0.000 threading.py:1103(daemon)
        4    0.000    0.000    0.000    0.000 threading.py:1185(_make_invoke_excepthook)
        1    0.000    0.000    0.000    0.000 threading.py:1238(Timer)
        1    0.000    0.000    0.000    0.000 threading.py:1268(_MainThread)
        1    0.000    0.000    0.000    0.000 threading.py:1270(__init__)
        1    0.000    0.000    0.000    0.000 threading.py:1289(_DummyThread)
        6    0.000    0.000    0.000    0.000 threading.py:1314(current_thread)
        1    0.000    0.000    0.000    0.000 threading.py:216(Condition)
        4    0.000    0.000    0.000    0.000 threading.py:228(__init__)
        4    0.000    0.000    0.000    0.000 threading.py:256(__enter__)
        4    0.000    0.000    0.000    0.000 threading.py:259(__exit__)
        3    0.000    0.000    0.000    0.000 threading.py:265(_release_save)
        3    0.000    0.000    0.000    0.000 threading.py:268(_acquire_restore)
        4    0.000    0.000    0.000    0.000 threading.py:271(_is_owned)
        3    0.000    0.000    0.000    0.000 threading.py:280(wait)
        1    0.000    0.000    0.000    0.000 threading.py:351(notify)
        1    0.000    0.000    0.000    0.000 threading.py:374(notify_all)
        1    0.000    0.000    0.000    0.000 threading.py:386(Semaphore)
        1    0.000    0.000    0.000    0.000 threading.py:469(BoundedSemaphore)
        1    0.000    0.000    0.000    0.000 threading.py:510(Event)
        4    0.000    0.000    0.000    0.000 threading.py:521(__init__)
        6    0.000    0.000    0.000    0.000 threading.py:529(is_set)
        1    0.000    0.000    0.000    0.000 threading.py:535(set)
        3    0.000    0.000    0.000    0.000 threading.py:556(wait)
        1    0.000    0.000    0.000    0.000 threading.py:589(Barrier)
        1    0.000    0.000    0.000    0.000 threading.py:743(BrokenBarrierError)
        3    0.000    0.000    0.000    0.000 threading.py:750(_newname)
        1    0.000    0.000    0.000    0.000 threading.py:766(Thread)
        4    0.000    0.000    0.000    0.000 threading.py:777(__init__)
        3    0.000    0.000    0.000    0.000 threading.py:851(start)
        1    0.000    0.000    0.000    0.000 threading.py:914(_set_ident)
        1    0.000    0.000    0.000    0.000 threading.py:918(_set_native_id)
        1    0.000    0.000    0.000    0.000 threading.py:921(_set_tstate_lock)
        1    0.000    0.000    0.000    0.000 threading.py:95(_RLock)
        3    0.000    0.000    0.000    0.000 threading.py:962(_stop)
        3    0.000    0.000   10.011    3.337 threading.py:997(join)
        3    0.000    0.000    0.000    0.000 {built-in method _imp._fix_co_filename}
       35    0.000    0.000    0.000    0.000 {built-in method _imp.acquire_lock}
        4    0.001    0.000    0.001    0.000 {built-in method _imp.create_dynamic}
        4    0.000    0.000    0.000    0.000 {built-in method _imp.exec_dynamic}
        7    0.000    0.000    0.000    0.000 {built-in method _imp.is_builtin}
        7    0.000    0.000    0.000    0.000 {built-in method _imp.is_frozen}
       35    0.000    0.000    0.000    0.000 {built-in method _imp.release_lock}
        1    0.000    0.000    0.000    0.000 {built-in method _thread._set_sentinel}
       23    0.000    0.000    0.000    0.000 {built-in method _thread.allocate_lock}
       21    0.000    0.000    0.000    0.000 {built-in method _thread.get_ident}
        1    0.000    0.000    0.000    0.000 {built-in method _thread.get_native_id}
        3    0.000    0.000    0.000    0.000 {built-in method _thread.start_new_thread}
       13    0.000    0.000    0.000    0.000 {built-in method builtins.__build_class__}
      4/1    0.000    0.000   10.016   10.016 {built-in method builtins.exec}
       42    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
       41    0.000    0.000    0.000    0.000 {built-in method builtins.hasattr}
       40    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
       19    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        9    0.000    0.000    0.000    0.000 {built-in method from_bytes}
        3    0.000    0.000    0.000    0.000 {built-in method io.open_code}
        3    0.000    0.000    0.000    0.000 {built-in method marshal.loads}
        1    0.000    0.000    0.000    0.000 {built-in method math.exp}
        2    0.000    0.000    0.000    0.000 {built-in method math.log}
        1    0.000    0.000    0.000    0.000 {built-in method math.sqrt}
       13    0.000    0.000    0.000    0.000 {built-in method posix.fspath}
        7    0.000    0.000    0.000    0.000 {built-in method posix.getcwd}
        2    0.000    0.000    0.000    0.000 {built-in method posix.register_at_fork}
       35    0.000    0.000    0.000    0.000 {built-in method posix.stat}
        1    0.000    0.000    0.000    0.000 {function Random.seed at 0x10232a430}
        4    0.000    0.000    0.000    0.000 {method '__enter__' of '_thread.lock' objects}
        3    0.000    0.000    0.000    0.000 {method '__exit__' of '_io._IOBase' objects}
       26    0.000    0.000    0.000    0.000 {method '__exit__' of '_thread.lock' objects}
       17   10.011    0.589   10.011    0.589 {method 'acquire' of '_thread.lock' objects}
        5    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}
        3    0.000    0.000    0.000    0.000 {method 'append' of 'collections.deque' objects}
        4    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        3    0.000    0.000    0.000    0.000 {method 'discard' of 'set' objects}
       11    0.000    0.000    0.000    0.000 {method 'endswith' of 'str' objects}
       14    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
      118    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
        3    0.000    0.000    0.000    0.000 {method 'locked' of '_thread.lock' objects}
        7    0.000    0.000    0.000    0.000 {method 'pop' of 'dict' objects}
        3    0.000    0.000    0.000    0.000 {method 'read' of '_io.BufferedReader' objects}
        6    0.000    0.000    0.000    0.000 {method 'release' of '_thread.lock' objects}
       51    0.000    0.000    0.000    0.000 {method 'rpartition' of 'str' objects}
      230    0.000    0.000    0.000    0.000 {method 'rstrip' of 'str' objects}
        2    0.000    0.000    0.000    0.000 {method 'setter' of 'property' objects}
'''
