list = ["apple", "banana", "cherry" , "blueberry", "grape"]
for name in list:
    if(name.startswith("e")):
        print(f"{name} starts with 'e'")
    else:
        print("does not start with 'e'")
        break
