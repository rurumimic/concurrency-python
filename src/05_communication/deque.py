import collections

doubleEndedQueue = collections.deque('123456')
print(f'Q: {doubleEndedQueue}')  # deque(['1', '2', '3', '4', '5', '6'])

for item in doubleEndedQueue:
    print(f'Item: {item}')

print(f'Left: {doubleEndedQueue[0]}')  # 1
print(f'Middle: {doubleEndedQueue[3]}')  # 4
print(f'Right: {doubleEndedQueue[-1]}')  # 6

doubleEndedQueue.remove('2')
print(f'Q: {doubleEndedQueue}')  # deque(['1', '3', '4', '5', '6'])

doubleEndedQueue.append('7')
print(f'Q: {doubleEndedQueue}')  # deque(['1', '3', '4', '5', '6', '7'])

doubleEndedQueue.appendleft('0')
print(f'Q: {doubleEndedQueue}')  # deque(['0', '1', '3', '4', '5', '6', '7'])

e = doubleEndedQueue.pop()  # 7
print(f'Q -{e}: {doubleEndedQueue}')  # deque(['0', '1', '3', '4', '5', '6'])

e = doubleEndedQueue.popleft()  # 0
print(f'Q -{e}: {doubleEndedQueue}')  # deque(['1', '3', '4', '5', '6'])

doubleEndedQueue.insert(1, '2')
print(f'Q: {doubleEndedQueue}')  # deque(['1', '2', '3', '4', '5', '6'])

doubleEndedQueue.rotate(3)
print(f'Q: {doubleEndedQueue}')  # deque(['4', '5', '6', '1', '2', '3'])

doubleEndedQueue.rotate(-2)
print(f'Q: {doubleEndedQueue}')  # deque(['6', '1', '2', '3', '4', '5'])
