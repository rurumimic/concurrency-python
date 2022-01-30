import random
import threading
import time


class Philosopher(threading.Thread):

    def __init__(self, name, leftFork, rightFork):
        print(f'{name} Has Sat Down At the Table')
        threading.Thread.__init__(self, name=name)
        self.leftFork = leftFork
        self.rightFork = rightFork

    def run(self):
        print(f'{threading.current_thread().name} has started thinking')
        while True:
            time.sleep(random.randint(1, 5))
            print(f'{threading.current_thread().name} has finished thinking')
            self.leftFork.acquire()
            time.sleep(random.randint(1, 5))
            try:
                print(
                    f'{threading.current_thread().name} has acquired the left fork')
                self.rightFork.acquire()
                try:
                    print(
                        f'{threading.current_thread().name} has attained both forks, currently eating')
                finally:
                    self.rightFork.release()
                    print(
                        f'{threading.current_thread().name} has released the right fork')
            finally:
                self.leftFork.release()
                print(
                    f'{threading.current_thread().name} has released the left fork')


fork1 = threading.RLock()
fork2 = threading.RLock()
fork3 = threading.RLock()
fork4 = threading.RLock()
fork5 = threading.RLock()

philosopher1 = Philosopher('Kant', fork1, fork2)
philosopher2 = Philosopher('Aristotle', fork2, fork3)
philosopher3 = Philosopher('Spinoza', fork3, fork4)
philosopher4 = Philosopher('Marx', fork4, fork5)
philosopher5 = Philosopher('Russell', fork5, fork1)

philosopher1.start()
philosopher2.start()
philosopher3.start()
philosopher4.start()
philosopher5.start()

philosopher1.join()
philosopher2.join()
philosopher3.join()
philosopher4.join()
philosopher5.join()
