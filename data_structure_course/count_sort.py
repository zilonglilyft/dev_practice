import random, copy
from cal_time import cal_time
@cal_time
def count_sort(li,max_num = 100):
    count = [0 for i in range(max_num + 1)]
    for i in li:
        count[i] += 1
    li.clear()
    for i, j in enumerate(count):
        for _ in range(j):
            li.append(i)
@cal_time
def sys_sort(li):
    li.sort()

li = [random.randint(0,100) for _ in range(1000)]
li1 = copy.deepcopy(li)
li2 = copy.deepcopy(li)
print(li)
count_sort(li1)
print(li1)
sys_sort(li2)
print(li2)

"""
1. Limits of count sort:
(1) it can only work with finite range
(2) it can only work with integer, not float

2. Time complexity of count sort: o(n)
"""