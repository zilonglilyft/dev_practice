def hanoi(n, a, b, c):
    if n > 0:
        hanoi(n-1, a, c, b)
        print('moving from %s to %s' %(a, c))
        hanoi(n - 1, b, a, c)

hanoi(3,'a','b','c')

"""
how many steps for if we need to move n plates from a to c?
h(n) = h(n-1) + 1 + h(n-1) = 2*h(n-1)+1 => 2^n
"""