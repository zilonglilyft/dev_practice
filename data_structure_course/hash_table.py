"""
1. What is hash table?
A hash table uses a hash function to compute an index, also called a hash code,
into an array of buckets or slots, from which the desired value can be found.
=> in Python, both set and dict are hash tables.
2. hash table highlights?
(1) values are unique (non duplicated)
(2) no order
(3) find, insert, remove can be performed at O(1) complexity
3. How to deal with conflict? (i.e. after hash function, different inputs return same value)
(1) within the same slot, use a linklist to store all the inputs => frequently used
(2) use nested hash functions => rarely use
"""
from linklist import LinkedList

class HashTable:
    def __init__(self, size = 101):
        self.size = size
        self.T = [LinkedList() for _ in range(self.size)] # this is the table to store the inputs after hash function

    def h(self, k): # hash function, convert the inputs into slot value
        return k % self.size

    def find(self, k): # check if k is already in the table. If so, do not add.
        i = self.h(k) # i is the slot index. each slot is a linked list
        return self.T[i].find(k)

    def insert(self, k):
        i = self.h(k)
        if self.find(k):
            print("Duplicated Values!")
        else:
            self.T[i].insertFront(k)

ht = HashTable()
ht.insert(50)
ht.insert(1)
ht.insert(101)
print(ht.find(20))