
def temp(f):
    return 5*(f-32)/9

f = int(input("Enter the temperature in Fahrenheit: "))
c = temp(f)
print(f"The temperature in Celsius is: {round(c, 2)}")