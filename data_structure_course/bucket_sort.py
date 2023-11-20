from cal_time import cal_time
@cal_time
def bucket_sort(li, n = 100, max_num = 10000):
    buckets = [[] for _ in range(n)]
    for var in li:
        pos = min(var//(max_num//n), n-1)
        buckets[pos].append(var)
        for i in range(len(buckets[pos])-1,0,-1):
            if buckets[pos][i-1] > buckets[pos][i]:
                buckets[pos][i - 1], buckets[pos][i] = buckets[pos][i], buckets[pos][i-1]
            else:
                break
    li.clear()
    for i in buckets:
        li+=i

import random
li = [random.randint(0,1000) for _ in range(10000)]
print(li)
bucket_sort(li)
print(li)

"""
1. logic of bucket sort
(1) it breaks down the original count sort in different buckets. This saves space the list is small while the range is large

2. complexity
(1) time complexity: best => o(n + k); worst => o(n**2 * k)
(2) space complexity: o(nk)
"""