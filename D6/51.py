# Task:
#   (a) Plot the functions y1 and y2 for the values of x Є [ 0 – 4Π ] and increment 0.1.:
#   y1= 2sin(x) - in blue -
#   y2= x cos(x) - in green -
#   (b) Do a second plot with the same functions but for the interval of x Є [ 2 - 3 ] and increment 0.01 

# -------------------------------------------------------------------------------------------------------
# Possible solution:
import math
import matplotlib.pyplot as plt

xs = [0] * int(4 * math.pi / 0.1 + 1)
y1 = xs.copy()
y2 = xs.copy()
i = 0
x = 0
while x <= 4*math.pi:
    xs[i] = x
    y1[i] = 2 * math.sin(x)
    y2[i] = x * math.cos(x)
    x += 0.1
    i += 1
plt.plot(xs, y1, 'b')
plt.plot(xs, y2, 'g')
plt.show()

xs = [0] * 101
y1 = xs.copy()
y2 = xs.copy()
i = 0
x = 2
while x <= 3:
    xs[i] = x
    y1[i] = 2 * math.sin(x)
    y2[i] = x * math.cos(x)
    x += 0.01
    i += 1
plt.plot(xs, y1, 'b')
plt.plot(xs, y2, 'g')
plt.show()

# -------------------------------------------------------------------------------------------------------
# Advanced solution.
# Using NumPy arrays with their vectorized operations:
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 4 * np.pi, 0.1)
y1 = 2 * np.sin(x)
y2 = x * np.cos(x)
plt.plot(x, y1, 'b')
plt.plot(x, y2, 'g')
plt.show()

x = np.arange(2, 3, 0.01)
y1 = 2 * np.sin(x)
y2 = x * np.cos(x)
plt.plot(x, y1, 'b')
plt.plot(x, y2, 'g')
plt.show()
