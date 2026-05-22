class employee:
    a = 1
    @classmethod # YOU CAN USE THIS TO SHOW CLASS ATTRIBUTE
    def show(cls):
        print(f"this is the class attribute of {cls.a}")
    
    @property
    def name(self):
        return (f"{self.fname} {self.lname}")
    
    @name.setter
    def name(self, value):
        self.ename = value
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]
e = employee()
e.a = 45
e.name = "david sindur"
print(e.fname, e.lname)
e.show()
