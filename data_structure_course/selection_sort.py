import random
def select_sort(li):
    for i in range(len(li)-1):
        min_ind = i
        for j in range(i+1, len(li)):
            if li[j] < li[min_ind]:
                min_ind = j
        li[i], li[min_ind] = li[min_ind], li[i]
    return li

li = [random.randint(0,10000) for i in range(1000)]
print(select_sort(li))
