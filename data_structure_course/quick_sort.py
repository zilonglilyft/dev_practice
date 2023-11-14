import random
from cal_time import cal_time
from insert_sort import insert_sort
import copy
def partition(li, left, right):
    tmp = li[left]
    while left < right:
        while left < right and li[right]>=tmp:
            right -= 1
        li[left] = li[right]
        while left < right and li[left]<=tmp:
            left += 1
        li[right] = li[left]
    li[left] = tmp
    return left

def _quick_sort(li, left, right):
    if left < right:
        mid = partition(li, left, right)
        _quick_sort(li, left, mid - 1)
        _quick_sort(li, mid + 1, right)
    return li

@cal_time
def quick_sort(li):
    _quick_sort(li, 0, len(li)-1)


li = [random.randint(0,100000) for i in range(10000)]
li_1 = copy.deepcopy(li)
li_2 = copy.deepcopy(li)
quick_sort(li_1)
print(li_1)
insert_sort(li_2)
print(li_2)



"""
time complexity of quick sort:
1. there will be log(n) recursion
2. each recursion will do one loop of n in total
3. so in total the time complexity is n*log(n)
"""