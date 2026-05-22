# What is the example of recursion
def factorial(n):

    """Calculate the factorial of     a number."""
    if (n == 0 or n == 1):
        return 1                    
    return n * factorial(n - 1) 
n = int(input("Enter a number: "))
print(f"the factorial of the entered number is: {factorial(n)}")