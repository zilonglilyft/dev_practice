def func1(x):
    if x > 0:
        print(x)
        func1(x-1)

def func2(x):
    if x > 0:
        func2(x-1)
        print(x)

func2(3)