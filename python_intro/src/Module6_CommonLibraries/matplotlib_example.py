''' 
Matplotlib is a widely-used open-source plotting library for Python that provides 
an object-oriented API for embedding plots into applications. It is highly customizable 
and supports a variety of plots, including line graphs, scatter plots, bar charts, 
and histograms. Matplotlib is essential for data visualization in data science and 
scientific computing.

Common Use Cases:
 - Creating static, animated, and interactive visualizations
 - Data exploration and presentation
 - Customizing plots with labels, titles, and legends
 - Integration with NumPy and Pandas for enhanced visualization

 https://matplotlib.org/stable/index.html
'''

# Importing the necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Creating data for plotting
x = np.linspace(0, 10, 100)  # 100 points from 0 to 10
y = np.sin(x)  # Sine function

# Creating the plot
plt.figure(figsize=(10, 5))  # Set the figure size
plt.plot(x, y, label='Sine Wave', color='blue')  # Plotting the sine wave

# Adding title and labels
plt.title('Sine Wave Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Adding a legend
plt.legend()

# Displaying the plot
plt.grid(True)  # Adding a grid
plt.savefig('sine_wave.png')  # Save the plot as a PNG file

