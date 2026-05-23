from functools import reduce
# map example
l = [1, 2, 3, 4, 5,]
square = lambda l: l*l
print(square)

sqlist = map(square, l)
print(list(sqlist))

# filter example
def even(n):
    if (n%2 == 0):
        return True
    return False

onlyeven = filter(square, l)
print(list(onlyeven))

# reduce example
def sum(a, b):
    return a + b
mul = lambda x,y:x*y
print(reduce(sum, l))
print(reduce(mul, l))