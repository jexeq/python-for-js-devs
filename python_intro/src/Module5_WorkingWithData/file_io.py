# File Input and Output in Python

# 1. Reading from a File
# Open a file and read its contents
with open('example.txt', 'r') as file:
    content = file.read()
    print("File Content:")
    print(content)

# 2. Writing to a File
# Write data to a file (overwriting existing content)
with open('output.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is a new line in the file.")

# 3. Appending to a File
# Append data to an existing file
with open('output.txt', 'a') as file:
    file.write("This line is appended to the file.\n")

# 4. Reading All Lines
# Read all lines from a file into a list
with open('output.txt', 'r') as file:
    lines = file.readlines()
    print("Lines from output.txt:")
    for line in lines:
        print(line.strip())

# 5. Handling File Not Found Error
try:
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError as e:
    print(f"Error: {e}")

# 6. Using 'with' Statement
# The 'with' statement ensures proper acquisition and release of resources
with open('example.txt', 'r') as file:
    content = file.read()
    print("Safely read file content:")
    print(content)
