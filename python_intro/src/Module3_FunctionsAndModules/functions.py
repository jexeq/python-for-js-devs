# English

# Functions in Python

# Functions are blocks of reusable code that perform a specific task.
# They help to modularize code and make it more organized and manageable.

# 1. Defining a Function
# Use the 'def' keyword to define a function.
# Example: Simple Function
def greet():
    print("Hello, World!")

# Call the function
greet()


# 2. Function with Parameters
# Functions can accept parameters to process input data.
# Example: Function with Parameters
def greet_person(name):
    print(f"Hello, {name}!")

# Call the function with an argument
greet_person("Alice")


# 3. Function with Return Value
# Functions can return values using the 'return' keyword.
# Example: Function with Return Value
def add(a, b):
    return a + b

# Call the function and store the result
result = add(5, 3)
print(f"5 + 3 = {result}")


# 4. Default Parameter Values
# You can provide default values for parameters.
# Example: Function with Default Parameter Values
def greet_with_default(name="Guest"):
    print(f"Hello, {name}!")

# Call the function without an argument
greet_with_default()

# Call the function with an argument
greet_with_default("Alice")


# 5. Keyword Arguments
# You can call functions with keyword arguments, specifying the parameter names.
# Example: Function with Keyword Arguments
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}.")

# Call the function with keyword arguments
describe_pet(animal_type="dog", pet_name="Buddy")
describe_pet(pet_name="Whiskers", animal_type="cat")


# 6. Variable-Length Arguments
# Functions can accept a variable number of arguments using *args and **kwargs.
# Example: Function with *args
def make_pizza(*toppings):
    print("Making a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

# Call the function with multiple arguments
make_pizza("pepperoni", "mushrooms", "green peppers")

# Example: Function with **kwargs
def build_profile(first, last, **user_info):
    profile = {'first_name': first, 'last_name': last}
    for key, value in user_info.items():
        profile[key] = value
    return profile

# Call the function with keyword arguments
user_profile = build_profile("albert", "einstein", location="princeton", field="physics")
print(user_profile)


# 7. Lambda Functions
# Lambda functions are small anonymous functions defined with the 'lambda' keyword.
# Example: Lambda Function
square = lambda x: x * x

# Call the lambda function
print(f"The square of 5 is {square(5)}")


# 8. Docstrings
# Docstrings are used to document functions. They are written as the first statement in the function.
# Example: Function with Docstring
def multiply(a, b):
    """
    Multiply two numbers and return the result.
    
    Parameters:
    a (int, float): The first number.
    b (int, float): The second number.
    
    Returns:
    int, float: The result of multiplying a and b.
    """
    return a * b

# Call the function and print the docstring
print(multiply(5, 3))
print(multiply.__doc__)


# 9. Nested Functions
# Functions can be defined inside other functions, creating nested functions.
# Example: Nested Function
def outer_function(text):
    def inner_function():
        print(text)
    inner_function()

# Call the outer function
outer_function("Hello from the nested function!")


# 10. Function Annotations
# Function annotations provide a way to attach metadata to function parameters and return values.
# Example: Function with Annotations
def greet_with_annotation(name: str) -> str:
    return f"Hello, {name}!"

# Call the function
print(greet_with_annotation("Alice"))
print(greet_with_annotation.__annotations__)

# --------------------------------------------------------------------------------------------------------------
