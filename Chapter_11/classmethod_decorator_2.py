class employee:
    a = 1
    @classmethod # YOU CAN USE THIS TO SHOW CLASS ATTRIBUTE
    def show(cls):
        print(f"this is the class attribute of {cls.a}")

e = employee()
e.a = 45
e.show()
        

'''
class employee:
    a = 1
    @classmethod
    def show(self):
        print(f"this is the class attribute of {self.a}")

e = employee()
e.a = 45
e.show()
'''
# THIS WILL IGNORE THE CLASS ATTRIBUTE