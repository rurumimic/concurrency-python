import threading
import random
import time


class Producer(threading.Thread):
    """
    Produces random integers to a list
    """

    def __init__(self, integers, condition):
        """
        Constructor.
        @param integers list of integers
        @param condition condition synchronization object
        """
        threading.Thread.__init__(self)
        self.integers = integers
        self.condition = condition

    def run(self):
        """
        Thread run method. Append random integers to the integers list
        at random time.
        """
        while True:
            integer = random.randint(0, 256)
            self.condition.acquire()
            print(f'condition acquired by {self.name}')
            self.integers.append(integer)
            print(f'{integer} appended to list by {self.name}')
            print(f'condition notified by {self.name}')
            self.condition.notify()
            print(f'condition released by {self.name}')
            self.condition.release()
            time.sleep(1)


class Consumer(threading.Thread):
    """
    Consumes random integers from a list
    """

    def __init__(self, integers, condition):
        """
        Constructor.
        @param integers list of integers
        @param condition condition synchronization object
        """
        threading.Thread.__init__(self)
        self.integers = integers
        self.condition = condition

    def run(self):
        """
        Thread run method. Consumes integers from list
        """
        while True:
            self.condition.acquire()
            print(f'condition acquired by {self.name}')
            while True:
                if self.integers:
                    integer = self.integers.pop()
                    print(f'{integer} popped from list by {self.name}')
                    break
                print(f'condition wait by {self.name}')
                self.condition.wait()
            print(f'condition released by {self.name}')
            self.condition.release()


def main():
    integers = []
    condition = threading.Condition()
    t1 = Producer(integers, condition)
    t2 = Consumer(integers, condition)
    t1.start()
    t2.start()
    t1.join()
    t2.join()


if __name__ == '__main__':
    main()


'''
condition acquired by Thread-1
37 appended to list by Thread-1
condition notified by Thread-1
condition released by Thread-1

condition acquired by Thread-2
37 popped from list by Thread-2
condition released by Thread-2
condition acquired by Thread-2
condition wait by Thread-2

condition acquired by Thread-1
207 appended to list by Thread-1
condition notified by Thread-1
condition released by Thread-1

207 popped from list by Thread-2
condition released by Thread-2
condition acquired by Thread-2
condition wait by Thread-2
'''
