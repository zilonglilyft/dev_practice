from cal_time import cal_time
def insert_sort_gap(li, gap):
    for i in range(gap, len(li)):
        tmp = li[i]
        j = i - gap
        while j >= 0 and li[j] > tmp:
            li[j+gap] =  li[j]
            j -= gap
        li[j+gap] = tmp

@cal_time
def shell_sort(li):
    gap = len(li)//2
    while gap>=1:
        insert_sort_gap(li, gap)
        gap = gap//2

import random
li = [i for i in range(10000)]
random.shuffle(li)
print(li)
shell_sort(li)
print(li)

"""
1. logic of shell sort
it is just an advanced version of insert sort. Instead of comparing one next to each other, 
it defines a fixed gap for each round, the given number will compare with the number with the gap interval,
and do the insert procedure.
The gap will decrease after each round until it becomes 1.

2. time complexity
With different choices of the gap sequence, the complexity are different.
In general, it is faster than simple insert sort, but it is slightly slower than heap sort.
"""