# Exception Handling in Python

# 1. Basic Try and Except
# Handling exceptions using try and except blocks
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError as e:
    print(f"Error: {e}")

# 2. Catching Multiple Exceptions
# You can catch multiple exceptions in one block
try:
    value = int("abc")  # This will raise a ValueError
except (ZeroDivisionError, ValueError) as e:
    print(f"Error: {e}")

# 3. Using Finally
# The finally block always executes, regardless of whether an exception occurred
try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError as e:
    print(f"Error: {e}")
finally:
    file.close()  # Ensure the file is closed

# 4. Raising Exceptions
# You can raise exceptions manually using the raise keyword
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

try:
    divide(10, 0)
except ValueError as e:
    print(f"Error: {e}")

# 5. Custom Exceptions
# Creating your own exception class
class CustomError(Exception):
    pass

def check_value(x):
    if x < 0:
        raise CustomError("Negative value error!")

try:
    check_value(-1)
except CustomError as e:
    print(f"Error: {e}")

# 6. Catching All Exceptions
# Use a general exception to catch any error type
try:
    # Example code that may raise various exceptions
    result = 10 / int("abc")  # This will raise a ValueError
except Exception as e:  # Catching all exceptions
    print(f"An error occurred: {e}")
