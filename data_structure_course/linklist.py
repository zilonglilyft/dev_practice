"""
Link list are composed of nodes. Each node includes two parts, the item representing the value,
and next represent the next item value.

There are two types of creating link list:
1. insert at the head
(1) create new node
(2) point the next of the node to be the current head
(3) point the head to the new created node

2. insert at the tail
(1) the linklist should have both head and tail variables
(2) create new node
(3) point the next of tail to be new node
(4) point the tail to be the new created node
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def create(self, data):
        self.head = ListNode(data[0])
        cur = self.head
        for i in data[1:]:
            node = ListNode(i)
            cur.next = node
            cur = cur.next

    def length(self): # O(N)
        count = 0
        cur = self.head
        while cur: # very common way to loop through the linklist. If no value, it will return False
            count += 1
            cur = cur.next
        return count

    def find(self, val): # O(N)
        cur = self.head
        while cur:
            if val == cur.val:
                return True
            cur = cur.next
        else:
            return False

    def insertFront(self, val):
        node = ListNode(val)
        node.next = self.head
        self.head = node

    def insertRear(self, val):
        node = ListNode(val)
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node

    def insertInside(self, index, val):
        assert index > 0, "wrong index!"
        assert index < self.length() - 1, "wrong index"
        count = 0
        cur = self.head
        while cur and count < index - 1:
            count += 1
            cur = cur.next

        if not cur:
            return 'Error'

        node = ListNode(val)
        node.next = cur.next
        cur.next = node

    def removeFront(self):
        assert self.length()>0, "the list is blank!"
        self.head = self.head.next

    def removeRear(self):
        if not self.head or not self.head.next:
            return 'Error'

        cur = self.head
        while cur.next.next:
            cur = cur.next
        cur.next = None

    def removeInside(self, index):
        count = 0
        cur = self.head

        while cur.next and count < index - 1:
            count += 1
            cur = cur.next

        if not cur:
            return 'Error'

        cur.next = cur.next.next

    def printll(self):
        assert self.length()>0, "the list is blank!"
        cur = self.head
        while cur:
            print(cur.val)
            cur = cur.next

ll = LinkedList()
ll.create([1,2,3,4])
ll.insertFront(5)
ll.insertRear(6)
ll.insertInside(4,7)
ll.removeFront()
ll.removeRear()
ll.removeInside(4)
ll.printll()

