def get_integer_from_user():
    """Prompt the user for an integer and return the value.

    If the user enters invalid input, raise ValueError so the caller
    can handle the error.
    """
    user_input = input("Enter a number: ")
    # Convert the entered text to an integer. This may raise ValueError.
    return int(user_input)

try:
    # Call the function and store the valid integer.
    a = get_integer_from_user()
    print(f"You entered: {a}")
except ValueError as e:
    # Handle the case when the input is not a valid integer.
    print(f"An error occurred: {e}")
finally:
    # This block runs regardless of whether an exception was raised.
    print("Program continues...")