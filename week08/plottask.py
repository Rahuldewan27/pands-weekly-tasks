# plottask.py
# histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2 
# and a plot of the function  h(x)=x3 in the range 0 to 10 on the one set of axes
# Author : Rahul Parvesh Dewan

# importing numpy and matplotlib libraries
import numpy as np
import matplotlib.pyplot as plt

# normal distribution of a 1000 values with a mean of 5 and standard deviation of 2
x = np.random.normal(loc=5, scale=2, size=1000)
#print(x) #This was to test the outcome of the above

# Define function of h(x)
def h(x):
    return x**3

# Generate x values from 0 to 10 and calculate y values using the function h(x)
x_values = np.linspace(0, 10)  # points between 0 and 10
y_values = h(x_values)

# Display the normal distrubtion as a histogram and plot of the function h(x)
plt.hist(x)
plt.plot(x_values, y_values)

# Add labels, titles and legend
plt.grid(True)
plt.xlabel('x')
plt.ylabel('Density / h(x)')
plt.title("Histogram of Normal Distribution and Plot of h(x)")
plt.legend(['h(x) = x^3'])

# Display the plot
plt.show()



# References:
#1. NumPy. (n.d.). numpy.random.normal. [https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html)
#2. w3schools. (n.d.). Python Matplotlib pyplot. [https://www.w3schools.com/python/matplotlib_pyplot.asp](https://www.w3schools.com/python/matplotlib_pyplot.asp)
#3. w3schools. (n.d.). Python Matplotlib Histograms. [https://www.w3schools.com/python/matplotlib_histograms.asp](https://www.w3schools.com/python/matplotlib_histograms.asp)
#4. NumPy. (n.d.). numpy.linspace. [https://numpy.org/doc/stable/reference/generated/numpy.linspace.html](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html)
