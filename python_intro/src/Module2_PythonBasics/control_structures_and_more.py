# Control Structures in Python
# Estructuras de Control en Python

# Python has various control structures to manage the flow of the program.
# Python tiene varias estructuras de control para gestionar el flujo del programa.

# 1. If Statements
# Sentencias If

# Basic If statement
# Sentencia If básica
x = 10
if x > 5:
    print("x is greater than 5")
    # x es mayor que 5

# If-Else statement
# Sentencia If-Else
y = 3
if y > 5:
    print("y is greater than 5")
else:
    print("y is not greater than 5")
    # y no es mayor que 5

# If-Elif-Else statement
# Sentencia If-Elif-Else
z = 8
if z > 10:
    print("z is greater than 10")
elif z == 8:
    print("z is equal to 8")
    # z es igual a 8
else:
    print("z is less than 10")

# 2. Comparison Operators
# Operadores de comparación

a = 10
b = 20
c = 10

# Equal to (==)
# Igual a (==)
if a == c:
    print("a is equal to c")
    # a es igual a c

# Not equal to (!=)
# No igual a (!=)
if a != b:
    print("a is not equal to b")
    # a no es igual a b

# Greater than (>)
# Mayor que (>)
if b > a:
    print("b is greater than a")
    # b es mayor que a

# Less than (<)
# Menor que (<)
if a < b:
    print("a is less than b")
    # a es menor que b

# Greater than or equal to (>=)
# Mayor o igual que (>=)
if a >= c:
    print("a is greater than or equal to c")
    # a es mayor o igual que c

# Less than or equal to (<=)
# Menor o igual que (<=)
if c <= b:
    print("c is less than or equal to b")
    # c es menor o igual que b

# Identity (is)
# Identidad (is)
if a is c:
    print("a is c")
    # a es c

# Identity (is not)
# Identidad (is not)
if a is not b:
    print("a is not b")
    # a no es b

# 3. For Loops
# Bucles For

# Basic for loop
# Bucle for básico
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
    # Imprime cada fruta en la lista

# For loop with range
# Bucle for con range
for i in range(5):
    print(i)
    # Imprime números del 0 al 4

# For loop with index using enumerate
# Bucle for con índice usando enumerate
for index, fruit in enumerate(fruits):
    print(index, fruit)
    # Imprime el índice y la fruta

# 4. While Loops
# Bucles While

# Basic while loop
# Bucle while básico
count = 5
while count > 0:
    print(count)
    count -= 1
    # Imprime el valor de count y luego lo decrementa

# While loop with break
# Bucle while con break
n = 10
while n > 0:
    print(n)
    if n == 5:
        break
        # Sale del bucle cuando n es igual a 5
    n -= 1

# While loop with continue
# Bucle while con continue
m = 10
while m > 0:
    m -= 1
    if m % 2 == 0:
        continue
        # Salta el resto del bucle si m es par
    print(m)
    # Imprime m si es impar

# 5. Nested Loops
# Bucles anidados

# Nested for loops
# Bucles for anidados
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")
        # Imprime los valores de i y j

# Nested while loops
# Bucles while anidados
a = 3
while a > 0:
    b = 2
    while b > 0:
        print(f"a: {a}, b: {b}")
        b -= 1
        # Imprime los valores de a y b
    a -= 1

# 6. Comprehensions
# Comprensiones

# List comprehension
# Comprensión de listas
squares = [x ** 2 for x in range(10)]
print(squares)
# Imprime una lista de cuadrados de 0 a 9

# Dictionary comprehension
# Comprensión de diccionarios
square_dict = {x: x ** 2 for x in range(10)}
print(square_dict)
# Imprime un diccionario con claves de 0 a 9 y sus cuadrados como valores

# Set comprehension
# Comprensión de conjuntos
unique_squares = {x ** 2 for x in range(10)}
print(unique_squares)
# Imprime un conjunto de cuadrados únicos de 0 a 9


### Type checking / Checkeo de tipos

# Type Checking in Python
# Verificación de tipos en Python

# 1. Using type()
# Usando type()
x = 10
print(type(x))  # Output: <class 'int'>
# Imprime: <class 'int'>
# This is similar to JavaScript's typeof
# Esto es similar a typeof en JavaScript

y = "Hello"
print(type(y))  # Output: <class 'str'>
# Imprime: <class 'str'>

# 2. Using isinstance()
# Usando isinstance()
print(isinstance(x, int))  # Output: True
# Imprime: True

print(isinstance(y, str))  # Output: True
# Imprime: True

# isinstance can also check for multiple types
# isinstance también puede verificar múltiples tipos
print(isinstance(y, (int, str)))  # Output: True
# Imprime: True

# Checking if an object is an instance of a specific class
# Verificación si un objeto es instancia de una clase específica

class Animal:
    pass

class Dog(Animal):
    pass

dog = Dog()
print(isinstance(dog, Dog))      # Output: True
# Imprime: True
print(isinstance(dog, Animal))   # Output: True
# Imprime: True
print(isinstance(dog, object))   # Output: True
# Imprime: True

# isinstance() vs. type()
# isinstance() verifica si un objeto es una instancia o una instancia de una subclase de una clase.
# type() solo devuelve el tipo del objeto y no tiene en cuenta las subclases.
a = Animal()
print(type(a) == Animal)          # Output: True
# Imprime: True
print(isinstance(a, Animal))      # Output: True
# Imprime: True

d = Dog()
print(type(d) == Animal)        # Output: False
                                # Imprime: False
print(isinstance(d, Animal))    # Output: True
                                # Imprime: True

# Checking None type
# Verificación del tipo None
n = None
print(type(n))  # Output: <class 'NoneType'>
# Imprime: <class 'NoneType'>

# Custom class type checking
# Verificación del tipo en clases personalizadas

class CustomClass:
    pass

instance = CustomClass()
print(type(instance))                     # Output: <class '__main__.CustomClass'>

print(isinstance(instance, CustomClass))  # Output: True


