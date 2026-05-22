n = int(input("Enter a number: "))
pro = 1

for i in range(1, n+1):
    pro = pro * i
print(f"The product of the first {n} natural numbers is: {pro}")