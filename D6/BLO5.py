# Task:
#   Assume having the vector G containing the training days of a list of persons. Write the
#   code to create a plot of the persons that has one / two / three / … / eight training sessions left before requiring a health check, 
#   which should be done after 100 training days. The plot should show
#   the sessions left to the health check in the x-axis and the number of persons in that situation in the
#   y-axis.
#   EXAMPLE: if G=[91,22,43,94,5,96,97,28,97,10,32,93,94,65,96,97,14] the plot we get is ...

# ------------------------------------------------------------------------------------------------------
# Possible solution
import matplotlib.pyplot as plt
G = [91,22,43,94,5,96,97,28,97,10,32,93,94,65,96,97,14]
xs = range(1, 9)
counts = [0] * 8
for i in range(len(G)):
    days_to_100 = 100 - G[i]
    if 1 <= days_to_100 <= 8:
        counts[days_to_100 - 1] += 1
plt.bar(xs, counts)
plt.show()

# ------------------------------------------------------------------------------------------------------
# Advanced solution.
# Using `numpy.histogram`: https://numpy.org/doc/stable/reference/generated/numpy.histogram.html
import matplotlib.pyplot as plt
import numpy as np

G = [91,22,43,94,5,96,97,28,97,10,32,93,94,65,96,97,14]
days_left = [100 - days for days in G]  # list comprehension: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
data = np.histogram(days_left, bins=8, range=(1, 8))[0]
plt.bar(range(1, 9), data)
