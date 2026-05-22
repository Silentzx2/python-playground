a = 43  # Declare a global variable 'a' and assign it the value 43.

def fun():
    global a  # Specify that 'a' inside this function refers to the global variable 'a'.
    a = 42  # Modify the global variable 'a' to 42.
    print(a)  # Print the value of 'a' (42) inside the function.

fun()  # Call the function 'fun', which modifies and prints the global variable 'a'.
print(a)  # Print the value of the global variable 'a' after the function call (42).