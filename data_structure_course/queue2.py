"""
Python has its embedded queue module and functions, actually more than the one-direction queue.
It is called deque, and essentially a two-side queue, meaning you can either enqueue in the front and dequeue
in the rear, or enqueue in the rear and dequeue in the front.
"""
from collections import deque

q = deque()
q.append(1)
q.append(2)
print(q.popleft())
q.appendleft(3)
q.appendleft(4)
print(q.pop())

"""
deque() function has several parameters:
1. initial value in the queue
2. max size. if beyond the max size, the front value will be automatically removed 
"""
q1 = deque([2,3,4],5)
q1.append(5)
q1.appendleft(1)
q1.append(6)
print(q1.popleft())
