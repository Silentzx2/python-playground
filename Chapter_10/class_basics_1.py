class employee:
    age = 19 # This is a class attribute
    language = "py"
name = employee()
name.name = "david" # This is a object attribute
print(name.name, name.age)
