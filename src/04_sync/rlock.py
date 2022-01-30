import threading
import time


class myWorker():

    def __init__(self):
        self.a = 1
        self.b = 2
        self.rlock = threading.RLock()

    def modifyA(self):
        with self.rlock:
            # Modifying A : RLock Acquired: True
            print(f'Modifying A : RLock Acquired: {self.rlock._is_owned()}')
            # <locked _thread.RLock object owner=4487022016 count=2 at 0x105797d40>
            print(f'{self.rlock}')
            self.a = self.a + 1
            time.sleep(5)

    def modifyB(self):
        with self.rlock:
            # Modifying B : RLock Acquired: True
            print(f'Modifying B : RLock Acquired: {self.rlock._is_owned()}')
            # <locked _thread.RLock object owner=4487022016 count=2 at 0x105797d40>
            print(f'{self.rlock}')
            self.b = self.b - 1
            time.sleep(5)

    def modifyBoth(self):
        with self.rlock:
            print('Rlock acquired, modifying A and B')
            # <locked _thread.RLock object owner=4487022016 count=1 at 0x105797d40>
            print(f'{self.rlock}')
            self.modifyA()
            # <locked _thread.RLock object owner=4487022016 count=1 at 0x105797d40>
            print(f'{self.rlock}')
            self.modifyB()

        # <unlocked _thread.RLock object owner=0 count=0 at 0x105797d40>
        print(f'{self.rlock}')


workerA = myWorker()
workerA.modifyBoth()

'''
Rlock acquired, modifying A and B
<locked _thread.RLock object owner=4487022016 count=1 at 0x105797d40>
Modifying A : RLock Acquired: True
<locked _thread.RLock object owner=4487022016 count=2 at 0x105797d40>
<locked _thread.RLock object owner=4487022016 count=1 at 0x105797d40>
Modifying B : RLock Acquired: True
<locked _thread.RLock object owner=4487022016 count=2 at 0x105797d40>
<unlocked _thread.RLock object owner=0 count=0 at 0x105797d40>
'''
