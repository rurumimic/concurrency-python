from array import array
from multiprocessing.connection import Listener

address = ('localhost', 6000)  # 'AF_INET'


with Listener(address, authkey=b'secret') as listener:
    with listener.accept() as connect:
        print('connection accepted from', listener.last_accepted)

        connect.send([2.25, None, 'junk', float])
        connect.send_bytes(b'hello')
        connect.send_bytes(array('i', [42, 1729]))

'''
connection accepted from ('127.0.0.1', 50059)
'''
