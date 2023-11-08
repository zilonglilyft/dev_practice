import random

def bubble_sort(li):
    for i in range(len(li)-1):
        exchange = False
        for j in range(len(li)-i-1):
            if li[j+1] < li[j]: # change to li[j+1] > li[j] if we want to sort in descending order
                li[j], li[j+1] = li[j+1], li[j]
                exchange = True
        if not exchange:
            return li
    else:
        return li

li = [random.randint(0,10000) for i in range(1000)]
print(bubble_sort(li))