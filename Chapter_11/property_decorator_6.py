class employee:
    @property
    def name(self):
        print(f"{self.fname} {self.lname}")
    
    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]
e = employee()
e.name = "david sindur"
print(e.fname, e.lname)

