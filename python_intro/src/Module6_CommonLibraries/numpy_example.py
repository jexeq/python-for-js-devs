# NumPy Example: Basic Operations

# Importing the NumPy library
import numpy as np

# 1. Creating Arrays
# Creating a 1D array
array_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:", array_1d)

# Creating a 2D array (matrix)
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", array_2d)

# 2. Array Properties
# Checking the shape of the array
print("Shape of 2D Array:", array_2d.shape)

# Checking the data type of the array
print("Data type of 2D Array:", array_2d.dtype)

# 3. Array Operations
# Element-wise addition
array_sum = array_1d + 5
print("Array after addition:", array_sum)

# Element-wise multiplication
array_product = array_1d * 2
print("Array after multiplication:", array_product)

# 4. Statistical Functions
# Calculating the mean
mean_value = np.mean(array_1d)
print("Mean of Array:", mean_value)

# Calculating the sum
sum_value = np.sum(array_1d)
print("Sum of Array:", sum_value)

# 5. Reshaping Arrays
# Reshaping a 1D array into a 2D array
reshaped_array = array_1d.reshape((5, 1))
print("Reshaped Array:\n", reshaped_array)

# 6. Array Slicing
# Slicing the array
sliced_array = array_1d[1:4]
print("Sliced Array:", sliced_array)

# 7. Indexing with Conditions
# Using boolean indexing to filter values
boolean_array = array_1d > 2
filtered_array = array_1d[boolean_array]
print("Filtered Array (values > 2):", filtered_array)
