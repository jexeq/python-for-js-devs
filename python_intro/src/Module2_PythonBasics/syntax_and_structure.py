# Python Syntax and Structure

# Python is known for its readability and simplicity. Here are the basic elements of Python syntax.
# Python es conocido por su legibilidad y simplicidad. Aquí están los elementos básicos de la sintaxis de Python.

# 1. Print Function
# The print function is used to output data to the console.
# La función print se utiliza para mostrar datos en la consola.
print("Hello, World!")

# 2. Variables
# Variables are used to store data. You don't need to declare the type explicitly.
# Las variables se utilizan para almacenar datos. No necesitas declarar el tipo explícitamente.
name = "Alice"
age = 30
# As a convention, it is common to use camelCase notation for those variables which value will not be overwritten.
# Como convención, es común usar notación camelCase para aquellas variables cuyo valor no se sobrescribirá.
ThisIsAContant = 450

# 3. Data Types
# Python supports various data types:
# Python admite varios tipos de datos:
# - String
# - Cadena
greeting = "Hello"
# - Integer
# - Entero
count = 10
# - Float - further we will see libraries for numbers
# - Flotante - más adelante veremos bibliotecas para números
price = 19.99
# - Boolean
# - Booleano
is_active = True

# 4. Comments
# Comments are used to explain code. They start with a # symbol.
# Los comentarios se utilizan para explicar el código. Comienzan con un símbolo #.
# This is a single-line comment
# Este es un comentario de una sola línea

"""
This is a multi-line comment
You can write explanations that span multiple lines.
"""
"""
Este es un comentario de varias líneas
Puedes escribir explicaciones que abarcan varias líneas.
"""

# 5. Indentation
# Python uses indentation to define the structure of code blocks.
# Python utiliza la indentación para definir la estructura de los bloques de código.
if age > 18:
    print("You are an adult.")
else:
    print("You are a minor.")
# Si la edad es mayor a 18, imprime "Eres un adulto". De lo contrario, imprime "Eres un menor".

# 6. Basic Data Structures
# Python has built-in data structures like lists, tuples, and dictionaries.
# Python tiene estructuras de datos incorporadas como listas, tuplas y diccionarios.

# List
# Lista
fruits = ["apple", "banana", "cherry"]
print(fruits)

# Tuple (immutable)
# Tupla (inmutable)
coordinates = (10.0, 20.0)
print(coordinates)

# Dictionary (key-value pairs)
# Diccionario (pares clave-valor)
person = {"name": "Alice", "age": 30}
print(person)

# 7. Control Structures
# Conditional statements
# Sentencias condicionales
if age < 18:
    print("Minor")
elif age < 65:
    print("Adult")
else:
    print("Senior")
# Si la edad es menor de 18, imprime "Menor". Si es menor de 65, imprime "Adulto". De lo contrario, imprime "Senior".

# Loops
# For loop
# Bucle for
for fruit in fruits:
    print(fruit)

# For Loop using index
# Bucle for usando indice

"""
The enumerate() function adds a counter to an iterable (like a list, tuple, or string) 
and returns it as an enumerate object, which is an iterable of tuples. 
Each tuple contains the index and the corresponding value.

La función enumerate() agrega un contador a un iterable (como una lista, tupla o cadena) 
y lo devuelve como un objeto enumerate, que es un iterable de tuplas.
 Cada tupla contiene el índice y el valor correspondiente.

"""
for index, fruit in enumerate(fruits):
    print(index, fruit)

# While loop
# Bucle while
countdown = 5
while countdown > 0:
    print(countdown)
    countdown -= 1

# 8. Functions
# Functions are defined using the def keyword.
# Las funciones se definen utilizando la palabra clave def.
def greet(name):
    return f"Hello, {name}!"
    
# Call the greet function
# Llama a la función greet
print(greet("Alice"))
