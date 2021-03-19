# Task:
#   Write a program that reads the 3 coefficients A, B, C of a second order polynomial
#   (A*X2+B*X+C), calculates the values of the polynomial for a sequence of X values from -100 to
#   +100 and displays a plot of the result

# ------------------------------------------------------------------------------------------------
# Solution:
import matplotlib.pyplot as plt

a = float(input("A: "))
b = float(input("B: "))
c = float(input("C: "))
step = 1
left_boundary = -100
right_boundary = 100
points_count = int((right_boundary - left_boundary) / step + 1)
xs = [0] * points_count
ys = [0] * points_count
x = left_boundary
index = 0
while x <= right_boundary:
    xs[index] = x
    ys[index] = a*x**2 + b*x + c
    x += step
    index += 1
plt.plot(xs, ys)
plt.show()

# ------------------------------------------------------------------------------------------------
# Advanced solution.
# Using NumPy with its vectorized operations on arrays
import matplotlib.pyplot as plt
import numpy as np

a = float(input("A: "))
b = float(input("B: "))
c = float(input("C: "))
step = 1
left_boundary = -100
right_boundary = 100
x = np.arange(left_boundary, right_boundary, step)  # https://numpy.org/doc/stable/reference/generated/numpy.arange.html
y = a*x**2 + b*x + c
plt.plot(x, y)
plt.show()
