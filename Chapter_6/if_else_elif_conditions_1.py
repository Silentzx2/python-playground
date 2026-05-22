# Example of conditions in Python
# The example of if else and elif statements in Python.
#  The if statement is used to test a condition. If the condition is true, 
# the code block under the if statement is executed. If the condition is false, 
# the code block under the else statement is executed. The elif statement is used to test multiple conditions.

user = int(input("Enter your age: "))
if user > 18:
    print("You are an adult.")
elif user == 0:
    print("Can you tell how do you even exist?")
    print("Please enter a valid age.")
else:
    print("You are not an adult.")