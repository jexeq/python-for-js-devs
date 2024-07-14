# Modules in Python

# A module is a file containing Python definitions and statements.
# Modules allow you to organize your Python code into reusable pieces.

# 1. Creating a Module
# To create a module, simply create a Python file with a .py extension.
# For example, create a file named my_module.py with the following content:
"""
# my_module.py
def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b
"""

# 2. Importing a Module
# You can import a module using the import statement.
# Example: Importing a module
import my_module

# Using the functions from the module
print(my_module.greet("Alice"))
print(f"5 + 3 = {my_module.add(5, 3)}")


# 3. Importing Specific Functions
# You can import specific functions from a module using the from keyword.
# Example: Importing specific functions
from my_module import greet, add

print(greet("Bob"))
print(f"10 + 5 = {add(10, 5)}")


# 4. Importing with an Alias
# You can give a module or function an alias using the as keyword.
# Example: Importing with an alias
import my_module as mm

print(mm.greet("Charlie"))
print(f"2 + 3 = {mm.add(2, 3)}")


# 5. The __name__ Variable
# Every module has a special variable called __name__.
# If the module is being run directly, __name__ is set to '__main__'.
# Example: Using __name__ in a module
if __name__ == "__main__":
    print("This module is being run directly.")
else:
    print("This module has been imported.")


# 6. Standard Library Modules
# Python has a rich standard library with many useful modules.
# Example: Using the math module
import math

print(f"Square root of 16 is {math.sqrt(16)}")
print(f"Value of pi is {math.pi}")


# 7. Creating Your Own Module
# To create your own module, create a new Python file and define functions or variables.
# Example: Creating a simple module (my_module.py)
"""
def multiply(a, b):
    return a * b
"""

# 8. Using Built-in Functions for Modules
# You can check if a module is available using the built-in dir() function.
# Example: Check the contents of a module
print(dir(math))


# 9. Module Search Path
# Python searches for modules in the directories listed in sys.path.
# Example: Checking module search path
import sys
print(sys.path)


# 10. Package Structure
# A package is a collection of modules organized in a directory hierarchy.
# You can create a package by placing an __init__.py file in a directory.
# Example: Directory structure for a package
"""
my_package/
    __init__.py
    module1.py
    module2.py
"""

# 11. Importing from a Package
# You can import modules from a package using dot notation.
# Example: Importing from a package
from my_package import module1
