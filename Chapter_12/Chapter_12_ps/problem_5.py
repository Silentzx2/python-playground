n = int(input("Enter a number: "))
table = [n * i for i in range(1, 11)]
with open("table.txt", "a") as f:
    f.write(str(table) + "\n")
    print("The table is present in a file called table.txt")