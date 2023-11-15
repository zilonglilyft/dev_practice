def merge(li, low, mid, high):
    i = low
    j = mid + 1
    tmp = [] # one drawback of merge sort => it requires additional space with complexity o(n)
    while i <= mid and j <= high:
        if li[i] <= li[j]:
            tmp.append(li[i])
            i += 1
        else:
            tmp.append(li[j])
            j += 1
    while i <= mid:
        tmp.append(li[i])
        i += 1
    while j <= high:
        tmp.append(li[j])
        j += 1
    li[low:high+1] = tmp

def merge_sort(li, low, high):
    if low < high: # must be less here. it guarantees at least 2 values to do another recursion
        mid = (low + high)//2
        merge_sort(li, low, mid)
        merge_sort(li, mid+1, high)
        merge(li, low, mid, high)

import random
li = [i for i in range(1000)]
random.shuffle(li)
print(li)
merge_sort(li,0,len(li)-1)
print(li)

"""
summary of quick/heap/merge sort:
1. all of them have the time complexity as o(nlogn)
2. according to experiments, the running speed slightly differ: quick < merge < heap
3. drawbacks:
(1) quick sort: at extreme case (original list is reversed), the time complexity could be o(n**2)
(2) merge sort: need extra space
(3) heap sort: slowest among the three

what is the stability of a sort algo?
An algo is stable if it keeps the original order of two equal values
e.g. [3,2,4,1,2,5]
After sorting, if the first 2 still comes before the second 2, it is called stable. Otherwise, it is not stable.

Among the 6 sort algos introduced:
1. bubble, insert, and merge sort are stable
2. selection, quick, heap are not stable
"""