from cal_time import cal_time
@cal_time
def binary_search(li, val):
    left = 0
    right = len(li) - 1
    while left <= right:
        mid = (left+right)//2
        if li[mid] == val:
            return mid
        elif li[mid] > val:
            right = mid - 1
        else:
            left = mid + 1
    else:
        return None
    # return None
li = list(range(1000000000))
print(binary_search(li, 32900000))

"""
to use binary search, the list must be sorted already. So even though it is way faster than linear search,
if the list is big and unsorted, and you only want search for very few values, do not use binary search.

If you need search a lot of values, then sort it first, and then use binary search
"""
