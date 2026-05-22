try:
    with open("file1.txt", "r") as file:
        print(file.read())
except Exception as e:
    print(e)

try:
    with open("file2.txt", "r") as file:
        print(file.read())
except Exception as e:
    print(e)

try:
    with open("file3.txt", "r") as file:
        print(file.read())
except Exception as e:
    print(e)

print("Program continues...")
