"""
We need to know what is tree before learning the heap sort:
1. full/perfect binary tree
each parent will have two children. One left, and one right
for a k-level tree, there will be 2**k - 1 nodes in total

2. complete binary tree
for a k level complete tree
(1) it is full for level down to k - 1
(2) for the last level, it could be not full, but only on the right side

3. max/min heap
(1) max heap: each internal node is greater than or equal to its children
(2) min heap: each internal node is smaller than or equal to its children

4. use list to store a binary tree
(1) first of all, write all the nodes from above to below, from left to right, sequentially.
(2) for each internal node i, its left and right children, if there are any, will be 2*i + 1 and 2*i + 2 respectively
(3) for a given child j, its parent will be (j-1)//2

5. logic of heap sort
(1) You have to make the list as a max heap first. This is the pre-requisite
(2) Once we have the max heap, do the following steps:
Step 1: Remove root node.
Step 2: Move the last element of last level to root. => map heap will not hold after this step
Step 3: Compare the value of this child node with its parent.
Step 4: If value of parent is less than child, then swap them.
Step 5: Repeat step 3 & 4 until Heap property holds.

6. how to build a heap
(1) start from the very bottom/last node with child, compare the value between parent/children, if the parent value is smaller, swap them
(2) do the same process for each parent node backward up
(3) if a parent node has children and grandchildren (i.e. more than 2 level), make sure it compares all the sub-levels to make the sub-portion as a max heap
"""
import random
from cal_time import cal_time
def sift (li, low, high):
    """
    :param li: the list to be sorted
    :param low: the top/parent of the heap
    :param high: the last child of the heap
    :return: a max heap
    这里其实就是做一次向下的调整
    """
    i = low
    j = 2 * i + 1 # start from left child
    tmp = li[low]
    while j <= high: # if j > high, it means i has reached the bottom level and cannot go further down
        if j+1 <= high and li[j] < li[j+1]: # choose right child if right child > left child
            j += 1
        if li[j] > tmp:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:
            li[i] = tmp # tmp stops at a non-bottom level
            break
    else: # this else step must be included, otherwise the tmp value will not be placed anywhere, and the list is incomplete
        li[i] = tmp # tmp stops at the bottom level

@cal_time
def heap_sort(li):
    """
    :param li: unsorted list
    :return: li: sorted list
    steps:
    1. build a heap
    2. remove the low, fill with the high
    3. do sift
    4. redo 2 and 3 until low meet high
    """
    n = len(li)
    for i in range((n-2)//2, -1, -1):
        sift(li, i, n-1)
    # code above will build the heap
    for i in range(len(li)-1, 0, -1):
        li[i], li[0] = li[0], li[i]
        sift(li, 0, i-1)


li = [i for i in range(10000)]
random.shuffle(li)
print(li)
heap_sort(li)
print(li)

"""
Follow-Ups:
1. time complexity
(1) sift complexity is log(n)
(2) build the heap is n*log(n), and sort is n*log(n)
(3) the overall complexity is n*log(n)

2. Python internal module of heap: heapq
import heapq
import random
li = [i for i in range(1000)]
random.shuffle(li)
heapq.heapify(li)
for i in range(len(li)):
    print(heapq.heappop(li), end = ',')
"""
