class employee:
    age = 19 # This is a class attribute
    language = "py"
    def getinfo(self): # You can make a function inside a class
        print(f"The language is {self.language}  The age is {self.age}")
    
    @staticmethod
    def greet():
        print("Good morning")
        
name = employee()
name.name = "david" # This is a object attribute
name.language = "java"
print(name.name, name.age)
# name.getinfo() both are the same 
employee.getinfo(name)