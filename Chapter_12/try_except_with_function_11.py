try:
    a = int(input("Enter a number: "))
    print(f"You entered: {a}")
except ValueError as e:
    print(f"An error occurred: {e}")

print("Program continues...")