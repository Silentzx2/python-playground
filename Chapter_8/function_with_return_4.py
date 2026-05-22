def greet_user(name, ending):
    """A simple function example."""
    print(f"good evening, {name}! {ending}")
    return "Greeting sent!" # This will return a string when the function is called.

a = greet_user("Alice", "Thank you") # This is a function call. It will execute the code inside the function.
print(a) # This will print None because the function does not return anything.