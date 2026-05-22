class employee:
    salary = 197856 # This is a class attribute
    language = "py"
    name = "david"
    def __init__(self, name, salary, language): # This is called dunder methods. which is automatically called. 
        self.name = name
        self.salary = salary
        self.language = language
    
    @staticmethod
    def greet():
        print("Good morning")

david = employee("nikhil", 3242342, "java")
print(david.language, david.salary, david.name)
# name.getinfo() both are same