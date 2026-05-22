#  Defination of walrus
# Walrus operator (:=) assigns len("Hello World") to variable n AND uses that value in the comparison
# This checks if the length of the string is greater than 10 characters
if (n := len("Hello World")) > 10:
    # If the condition is true, print a message showing the string length
    print(f"String is too long ({n} characters)") 
