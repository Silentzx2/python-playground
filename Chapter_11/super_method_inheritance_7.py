class employee:
    def __init__(self):
        print("this is constructor of employee")
    a = 1

class coder(employee):
    def __init__(self):
        super().__init__()
        print("this is constructor of coder")
    b = 2
    
class programmer(coder):
    def __init__(self):
        super().__init__()
        print("this is constructor of programmer")
    c = 3


o = programmer()
print(o.a) # print a attribute
# print(o.b) # show a error as there no b attribute in class employee
