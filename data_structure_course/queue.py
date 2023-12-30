"""
Apparently in Python we can use list to create queue with the similar logic as stack.
However, since queue is "FIFO", the time complexity of either push or pop (depends on the definition) can be
huge if the list is large (O(n)).
So is there a way to create queue with time complexity be O(1), same as stack?
The answer is yes.
To realize it:
1. initialize a list with fixed size
2. initialize two pointers, one front and one rear
3. when enqueue, rear + 1. If rear reach the max size, start over from index 0
4. when out queue, front + 1. If front reach the max size, start over from index 0
5. The queue is empty when front = rear
6. The queue is full when (rear + 1) % max_size = front

By using two pointers, both enqueue and out queue are O(1) process
"""


class Queue:
    def __init__(self, size = 100):
        self.queue = [0 for _ in range(size)]
        self.size = size
        self.front = 0
        self.rear = 0

    def push(self, item):
        if not self.is_full():
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = item
        else:
            raise IndexError("The queue is full, cannot enqueue")

    def pop(self):
        if not self.is_empty():
            self.front = (self.front + 1) % self.size
            return self.queue[self.front] # similar to python list pop, here returns the element got dequeued
        else:
            raise IndexError("Queue is empty, cannot dequeue")

    def is_empty(self):
        return self.rear == self.front

    def is_full(self):
        return (self.rear+1) % self.size == self.front

queue = Queue(5)
for i in range(4):
    queue.push(i)
print(queue.pop())
queue.push(100)
print(queue.is_full())
print(queue.is_empty())