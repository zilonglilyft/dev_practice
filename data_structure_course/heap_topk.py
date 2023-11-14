"""
Find the largest k numbers from a list with length n. (n>k)
1. quick sort: nlog(n)
2. bubble/select/insert sort: kn
3. heap sort: nlog(k)

how:
1. use the first k number to build a min heap
2. loop through the rest value:
(1) if the value is less than the top/root node, then pass
(2) if the value is larger than the top/root node, replace the node, and then do a sift
"""

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
        if j+1 <= high and li[j] > li[j+1]: # choose right child if right child > left child
            j += 1
        if li[j] < tmp:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:
            li[i] = tmp # tmp stops at a non-bottom level
            break
    else: # this else step must be included, otherwise the tmp value will not be placed anywhere, and the list is incomplete
        li[i] = tmp # tmp stops at the bottom level

def heap_topk(li, k):
    tmp = li[0:k]
    for i in range((k-2)//2, -1, -1):
        sift(tmp, i, k-1)
    # above code build a small heap
    for j in range(k, len(li)):
        if li[j] > tmp[0]:
            tmp[0] = li[j]
            sift(tmp, 0, k-1)
    # above code find the largest k in the list
    for i in range(k-1,0,-1):
        tmp[i], tmp[0] = tmp[0], tmp[i]
        sift(tmp, 0, i-1)
    # above code sorted the top k values
    return tmp

import random
li = [i for i in range(1000)]
random.shuffle(li)
print(li)
print(heap_topk(li,100))