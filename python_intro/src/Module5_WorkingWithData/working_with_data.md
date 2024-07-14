# Working with Data in Python

## File Input and Output

### Comparison with JavaScript

| Operation           | Python                             | JavaScript                                                                     |
| ------------------- | ---------------------------------- | ------------------------------------------------------------------------------ |
| Reading a file      | `with open('file.txt', 'r') as f:` | `const fs = require('fs'); fs.readFile('file.txt', 'utf8', (err, data) => {})` |
| Writing to a file   | `with open('file.txt', 'w') as f:` | `fs.writeFile('file.txt', 'data', (err) => {})`                                |
| Reading all lines   | `lines = f.readlines()`            | `const lines = data.split('\n');`                                              |
| Appending to a file | `with open('file.txt', 'a') as f:` | `fs.appendFile('file.txt', 'data', (err) => {})`                               |

## Exception Handling

### Comparison with JavaScript

| Feature            | Python                              | JavaScript                         |
| ------------------ | ----------------------------------- | ---------------------------------- |
| Try-Except Block   | `try:`<br> `except Exception as e:` | `try { } catch (e) { }`            |
| Finally Block      | `finally:`                          | `finally { }`                      |
| Raising Exceptions | `raise ValueError("Error message")` | `throw new Error("Error message")` |

## Common Use Cases

1. **Reading from Files**: Use Python's built-in `open()` function to read from files efficiently.
2. **Writing to Files**: Use the `write()` method to store data into files.
3. **Handling Errors**: Implement exception handling to manage potential errors while performing file operations.

## Conclusion

Understanding how to work with data, including file I/O and exception handling, is essential for developing robust applications in Python. The similarities with JavaScript make transitioning between the two languages easier for developers.
