import collections

doubleEndedQueue = collections.deque('123456')
print(f'Q: {doubleEndedQueue}')  # deque(['1', '2', '3', '4', '5', '6'])

doubleEndedQueue.append('7')
print(f'Q: {doubleEndedQueue}')  # deque(['1', '3', '4', '5', '6', '7'])

doubleEndedQueue.appendleft('0')
print(f'Q: {doubleEndedQueue}')  # deque(['0', '1', '3', '4', '5', '6', '7'])
