# Object-Oriented Programming (OOP) in Python

Object-Oriented Programming (OOP) is a programming paradigm that uses "objects" to design applications. Python supports OOP, allowing you to create classes and manage objects.

## Classes and Objects

- **Class**: A blueprint for creating objects.
- **Object**: An instance of a class.

### Comparison with JavaScript

| Feature            | Python                | JavaScript                    |
| ------------------ | --------------------- | ----------------------------- |
| Class Definition   | `class Dog:`          | `class Dog {}`                |
| Object Creation    | `my_dog = Dog()`      | `const myDog = new Dog();`    |
| Self / This        | `self.name`           | `this.name`                   |
| Constructor        | `def __init__(self):` | `constructor() {}`            |
| Inheritance Syntax | `class Dog(Animal):`  | `class Dog extends Animal {}` |
| Super              | `super().__init__()`  | `super()`                     |

## 2. Attributes and Methods

- **Attributes**: Variables that belong to an object.
- **Methods**: Functions defined inside a class.

### Example

```python
class Cat:
    def __init__(self, name):
        self.name = name

    def meow(self):
        return f"{self.name} says meow!"
```
