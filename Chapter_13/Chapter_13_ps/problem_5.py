from functools import reduce
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 234, 38456]
def big(a,b):
    if (a>b):
        return a
    return b
    
print(reduce(big, l))