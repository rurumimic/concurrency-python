from array import array
from multiprocessing.connection import Client

address = ('localhost', 6000)  # 'AF_INET'


with Client(address, authkey=b'secret') as connect:
    print(connect.recv())  # [2.25, None, 'junk', <class 'float'>]
    print(connect.recv_bytes())  # b'hello'

    arr = array('i', [0, 0, 0, 0, 0])
    print(connect.recv_bytes_into(arr))  # 8
    print(arr)  # array('i', [42, 1729, 0, 0, 0])

'''
[2.25, None, 'junk', <class 'float'>]
b'hello'
8
array('i', [42, 1729, 0, 0, 0])
'''
