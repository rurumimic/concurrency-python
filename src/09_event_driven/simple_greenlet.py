import gevent
from gevent import Greenlet


def myGreenlet():
    print('My Greenlet is executing')


class MyNoopGreenlet(Greenlet):

    def __init__(self, seconds):
        Greenlet.__init__(self)
        self.seconds = seconds

    def _run(self):
        print('My Greenlet executing')
        gevent.sleep(self.seconds)

    def __str__(self):
        return f'MyNoopGreenlet{self.seconds}'


if __name__ == "__main__":
    gevent.spawn(myGreenlet)
    gevent.sleep(1)

    g = MyNoopGreenlet(2)
    g.start()
    g.join()
    print(g.dead)

'''
My Greenlet is executing

# sleep 1

My Greenlet executing

# sleep 2

True
'''
