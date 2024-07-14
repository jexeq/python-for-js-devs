# Object-Oriented Programming (OOP) in Python

# Python supports object-oriented programming, which allows you to create and manage objects and classes.

# 1. Classes and Objects

# A class is a blueprint for creating objects. An object is an instance of a class.

class Dog:
    """A simple Dog class."""
    
    def __init__(self, name, age):
        """Initialize the dog with a name and age."""
        self.name = name
        self.age = age
        
    def bark(self):
        """Make the dog bark."""
        return f"{self.name} says woof!"

# Creating an object of the Dog class
my_dog = Dog("Buddy", 3)
print(my_dog.bark())  # Output: Buddy says woof!

# 2. Attributes and Methods

# Attributes are variables that belong to an object. Methods are functions defined inside a class.

class Cat:
    """A simple Cat class."""
    
    def __init__(self, name, age):
        """Initialize the cat with a name and age."""
        self.name = name
        self.age = age
        
    def meow(self):
        """Make the cat meow."""
        return f"{self.name} says meow!"

# Creating an object of the Cat class
my_cat = Cat("Whiskers", 5)
print(my_cat.meow())  # Output: Whiskers says meow!

# 3. Inheritance

# Inheritance allows a class to inherit attributes and methods from another class.

class Animal:
    """A simple Animal class."""
    
    def __init__(self, species):
        """Initialize the animal with a species."""
        self.species = species

    def sound(self):
        """Return a generic sound."""
        return "Some sound"

class Bird(Animal):
    """A simple Bird class inheriting from Animal."""
    
    def __init__(self, name, species):
        super().__init__(species)
        self.name = name
        
    def sound(self):
        """Return the sound a bird makes."""
        return f"{self.name} says chirp!"

# Creating an object of the Bird class
my_bird = Bird("Tweety", "Canary")
print(my_bird.sound())  # Output: Tweety says chirp!

# 4. Encapsulation

# Encapsulation is the concept of restricting access to certain attributes and methods.

class Person:
    """A simple Person class."""
    
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # Private attribute
    
    def get_age(self):
        """Return the age of the person."""
        return self.__age

# Creating an object of the Person class
person = Person("Alice", 30)
print(person.name)      # Output: Alice
print(person.get_age()) # Output: 30
# print(person.__age)   # This will raise an AttributeError

# 5. Polymorphism

# Polymorphism allows methods to do different things based on the object it is acting upon.

class Fish(Animal):
    """A simple Fish class inheriting from Animal."""
    
    def __init__(self, name, species):
        super().__init__(species)
        self.name = name
        
    def sound(self):
        """Return the sound a fish makes."""
        return f"{self.name} makes blub blub!"

# Demonstrating polymorphism
def animal_sound(animal):
    print(animal.sound())

animal_sound(my_bird)  # Output: Tweety says chirp!
# animal_sound(my_dog)   # Output: Buddy says woof!
animal_sound(Fish("Nemo", "Clownfish"))  # Output: Nemo makes blub blub!

# Conclusion
# Object-oriented programming in Python helps to create structured and reusable code by utilizing classes and objects.
