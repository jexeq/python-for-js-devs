'''
Pandas is a powerful open-source data manipulation and analysis library for Python. 
It provides data structures like Series and DataFrame, which are designed to handle 
and analyze structured data efficiently. Pandas makes it easy to clean, transform, 
and visualize data, making it a staple for data science and analytics.

Common Use Cases:
 - Data cleaning and preparation
 - Data exploration and analysis
 - Time series analysis
 - Integration with other libraries like NumPy and Matplotlib

    https://pandas.pydata.org/docs/

'''

# Importing the pandas library
import pandas as pd

# Creating a simple DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}

df = pd.DataFrame(data)

# Displaying the DataFrame
print("DataFrame:")
print(df)

# Accessing a specific column
print("\nNames:")
print(df["Name"])

# Filtering the DataFrame
print("\nPeople older than 28:")
print(df[df["Age"] > 28])

# Adding a new column
df["Salary"] = [70000, 80000, 90000]
print("\nDataFrame with Salary:")
print(df)

# Saving the DataFrame to a CSV file
df.to_csv("people.csv", index=False)
print("\nDataFrame saved to 'people.csv'")
