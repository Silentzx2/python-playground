def sum(n):

    """Calculate the sum of the first n natural numbers."""
    if (n == 0 or n == 1):
        return 1                    
    return sum(n - 1) + n
n = int(input("Enter a number: "))
print(f"the sum of the first {n} natural numbers is: {sum(n)}")