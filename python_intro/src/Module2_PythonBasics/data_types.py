# Data Types in Python
# Tipos de datos en Python

# Python supports several built-in data types that can be categorized into mutable and immutable types.
# Python admite varios tipos de datos incorporados que se pueden clasificar en tipos mutables e inmutables.

# | Python Data Type | JavaScript Equivalent | Description                                |
# |------------------|-----------------------|--------------------------------------------|
# | str              | String                | Represents text.                           |
# | int              | Number                | Represents whole numbers.                  |
# | float            | Number                | Represents decimal numbers.                |
# | bool             | Boolean               | Represents true/false values.              |
# | list             | Array                 | Ordered, mutable collection of items.      |
# | tuple            | Array (immutable)     | Ordered, immutable collection of items.    |
# | dict             | Object                | Key-value pairs.                           |
# | set              | Set                   | Unordered collection of unique items.      |

# 1. Numbers
# 1. Números
# Python has three main numeric types: int, float, and complex.
# Python tiene tres tipos numéricos principales: int, float y complex.

# Integer
# Entero
integer_example = 42
print(f"Integer: {integer_example}")

# Float
# Flotante
float_example = 3.14
print(f"Float: {float_example}")

# Complex
# Complejo
complex_example = 1 + 2j
print(f"Complex: {complex_example}")

# 2. Strings
# 2. Cadenas
# Strings are sequences of characters enclosed in single or double quotes.
# Las cadenas son secuencias de caracteres encerradas en comillas simples o dobles.

# String
# Cadena
string_example = "Hello, World!"
print(f"String: {string_example}")

# Multi-line string
# Cadena de múltiples líneas
multi_line_string = """This is a
multi-line string."""
print(multi_line_string)

# Common String Methods
# Métodos comunes para cadenas
print(f"Uppercase: {string_example.upper()}")  # Converts to uppercase / Convierte a mayúsculas
print(f"Lowercase: {string_example.lower()}")  # Converts to lowercase / Convierte a minúsculas
print(f"Length: {len(string_example)}")  # Returns the length of the string / Retorna la longitud de la cadena
print(f"Split: {string_example.split(',')}")  # Splits the string into a list / Divide la cadena en una lista
print(f"Replace: {string_example.replace('World', 'Python')}")  # Replaces a substring / Reemplaza una subcadena

# 3. Lists
# 3. Listas
# Lists are ordered, mutable collections of items.
# Las listas son colecciones ordenadas y mutables de elementos.

# List
# Lista
list_example = [1, 3, 2, 4, 5]
print(f"List: {list_example}")

# Common List Methods
# Métodos comunes para listas
list_example.append(6)  # Adds an item to the end / Agrega un elemento al final
print(f"Appended List: {list_example}")
print(f"Pop: {list_example.pop()}")  # Removes and returns the last item / Elimina y retorna el último elemento
print(f"Sorted List: {sorted(list_example)}")  # Returns a sorted copy of the list / Retorna una copia ordenada de la lista
list_example.insert(0, 0)  # Inserts an item at a specified position / Inserta un elemento en una posición específica
print(f"Inserted List: {list_example}")
print(f"Count of 2: {list_example.count(2)}")  # Counts occurrences of a value / Cuenta las ocurrencias de un valor

# 4. Tuples
# 4. Tuplas
# Tuples are ordered, immutable collections of items.
# Las tuplas son colecciones ordenadas e inmutables de elementos.

# Tuple
# Tupla
tuple_example = (1, 2, 3)
print(f"Tuple: {tuple_example}")

mixed_tuple = (42, "Hello", 3.14, True)
print(f"Mixed Tuple: {mixed_tuple}")

# Common Tuple Methods
# Métodos comunes para tuplas
print(f"Tuple Length: {len(tuple_example)}")  # Returns the length of the tuple / Retorna la longitud de la tupla
print(f"Tuple Index: {tuple_example.index(2)}")  # Finds index of a value / Encuentra el índice de un valor
print(f"Count of 1: {tuple_example.count(1)}")  # Counts occurrences of a value / Cuenta las ocurrencias de un valor

# 5. Dictionaries
# 5. Diccionarios
# Dictionaries are unordered collections of key-value pairs.
# Los diccionarios son colecciones no ordenadas de pares clave-valor.

# Dictionary
# Diccionario
dict_example = {"name": "Alice", "age": 30}
print(f"Dictionary: {dict_example}")

# Common Dictionary Methods
# Métodos comunes para diccionarios
print(f"Keys: {dict_example.keys()}")  # Returns a view of the dictionary's keys / Retorna una vista de las claves del diccionario
print(f"Values: {dict_example.values()}")  # Returns a view of the dictionary's values / Retorna una vista de los valores del diccionario
print(f"Get Name: {dict_example.get('name')}")  # Retrieves a value by key / Recupera un valor por clave
dict_example["age"] = 31  # Updates the value associated with a key / Actualiza el valor asociado con una clave
print(f"Updated Dictionary: {dict_example}")
dict_example.setdefault("city", "New York")  # Sets a default value if the key does not exist / Establece un valor por defecto si la clave no existe
print(f"Dictionary with default city: {dict_example}")

# 6. Sets
# 6. Conjuntos
# Sets are unordered collections of unique items.
# Los conjuntos son colecciones no ordenadas de elementos únicos.

# Set
# Conjunto
set_example = {1, 2, 3, 4, 4, 5}
print(f"Set: {set_example}")  # Duplicates are removed / Se eliminan los duplicados

# Common Set Methods
# Métodos comunes para conjuntos
set_example.add(6)  # Adds an item to the set / Agrega un elemento al conjunto
print(f"Updated Set: {set_example}")
set_example.remove(3)  # Removes an item; raises KeyError if not found / Elimina un elemento; genera KeyError si no se encuentra
print(f"Set after removal: {set_example}")
set_example.discard(2)  # Removes an item; does not raise an error if not found / Elimina un elemento; no genera un error si no se encuentra
print(f"Set after discarding 2: {set_example}")
print(f"Set Length: {len(set_example)}")  # Returns the number of unique items / Retorna el número de elementos únicos

# Summary of Data Types
# Resumen de tipos de datos:
# - Numbers: int, float, complex / Números: int, float, complex
# - Strings: str / Cadenas: str
# - Lists: list / Listas: list
# - Tuples: tuple / Tuplas: tuple
# - Dictionaries: dict / Diccionarios: dict
# - Sets: set / Conjuntos: set
