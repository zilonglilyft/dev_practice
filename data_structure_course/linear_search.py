from cal_time import cal_time
@cal_time
def linear_search(li, val):
    for ind, v in enumerate(li):
        if v == val:
            return ind
    return None

li = list(range(1000000000))
print(linear_search(li, 32900000))

"""
python internal index() function is just using linear search algo, because the list is not by default sorted
for most of the time

a = [1,2,3,4,5]
print(a.index(2)) => 1
"""