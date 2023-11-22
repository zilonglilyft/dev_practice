from cal_time import cal_time
@cal_time
def radix_sort(li):
    # 1. determine how many iterations
    max_num = max(li)
    _iter = 0
    while 10**_iter<=max_num:
        # 2. iter to order from the smaller digit all the way to larger
        buckets = [[] for _ in range(10)]
        for val in li:
            digit = (val//(10**_iter))%10 # This step determine the number with the corresponding digit.
            buckets[digit].append(val)
        # 3. rearrange the list based on the order with the current digit
        li.clear()
        for buc in buckets:
            li += buc
        _iter += 1

import random
li = [random.randint(0,1000) for _ in range(10000)]
random.shuffle(li)
print(li)
radix_sort(li)
print(li)

"""
logic of radix sort
1. within each iteration, the bucket is fixed and ordered (from 0 to 9). This guarantees that the corresponding
digit within each iteration is ordered
2. iterate start from the smallest digit all the way to the maximum digit. This guarantees that the largest digit
is ordered with the top priority.
3. The time complexity is o(n*log10(max_num)). In other word, the efficiency of radix sort 
partially depends on the distribution of the numbers.
In most cases though, radix sort is even faster than quick/merge/heap sort.
4. it can be slower than quick sort when n is small, while max_num is very large
5. by default it only works for positive integers. This is one disadvantage.
6. it borrows the bucket sort concept.
7. radix sort can also be used in sort on strings. The difference is that for numbers, it lined up based on the tail.
While for strings, it lined up on head. Also for characters, the bucket size should be 26 instead of 10.
"""