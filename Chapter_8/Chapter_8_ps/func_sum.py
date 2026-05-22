# Write a program to find the greatest of three
# numbers entered by the user.
def greatest(a, b, c):
    if (a >= b) and (a >= c):
        return a
    elif (b >= a) and (b >= c):
        return b
    else:
        return c
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))
print(f"The greatest of the three numbers is: {greatest(a, b, c)}")