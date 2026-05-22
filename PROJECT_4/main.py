try:

    option = int(input("Enter the operation you want to perform (1 for add, 2 for subtract, 3 for multiply, 4 for divide): "))

    match option:
        case 1:
            a = int(input("Enter a number: "))
            b = int(input("Enter a number: "))
            print(f"You entered {a} and {b}")
            print(a + b)
        case 2:
            a = int(input("Enter a number: "))
            b = int(input("Enter a number: "))
            print(f"You entered {a} and {b}")
            print(a - b)
        case 3:
            a = int(input("Enter a number: "))
            b = int(input("Enter a number: "))
            print(f"You entered {a} and {b}")
            print(a * b)
        case 4:
            a = int(input("Enter a number: "))
            b = int(input("Enter a number: "))
            print(f"You entered {a} and {b}")
            print(a / b)
except ValueError as v:
    print("Enter a valid number")

