import random
from cal_time import cal_time
@cal_time
def insert_sort(li):
    for i in range(1, len(li)):
        tmp = li[i]
        j = i - 1
        while j >= 0 and li[j] > tmp:
            li[j+1], li[j] = li[j], li[j+1]
            j -= 1


li = [random.randint(0,100000) for i in range(10000)]
insert_sort(li)
print(li)