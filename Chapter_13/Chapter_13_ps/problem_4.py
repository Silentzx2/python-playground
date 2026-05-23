
def dev(n):
    if (n%5 == 0):
       return True
    return False
a = [1,2,3,4,5,6,7,8,9,10]
f = list(filter(dev, a))
print(f)