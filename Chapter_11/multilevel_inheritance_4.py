class employee:
    a = 1

class coder(employee):
    b = 2
    
class programmer(coder):
    c = 3


o = employee()
print(o.a) # print a attribute
# print(o.b) # show a error as there no b attribute in class employee

o = programmer()
print(o.a, o.b)

o = coder()
print(o.a, o.b)