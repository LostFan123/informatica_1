# Task:
#   Write a program that reads from keyboard the coordinates (x,y) of 2 points in the plane (2D)
#   and calculates the Euclidean distance between both points. For instance, in we enter the points
#   (3, 5) and (6,1), the programs responds with value 5

# ------------------------------------------------------------------------------------------------

# Possible solution
x1 = float(input("x1: "))
y1 = float(input("y1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print(distance)

# Alternatively one can use `math.sqrt`:
import math
x1 = float(input("x1: "))
y1 = float(input("y1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(distance)

# ------------------------------------------------------------------------------------------------

# Advanced solution: 
#   One can use `math.dist` function. 
#   See: https://docs.python.org/3/library/math.html#math.dist
#   Note that it expects two parameters which should be iterables.
#   In short, an iterable is something that can be looped over like a string, a list, a file, etc.
#   In this case we use two "tuples": (x1, y1) and (x2, y2). 
#   Tuples are somewhat similar to lists. For the discussion on their differences see https://stackoverflow.com/q/626759/7851470
import math
x1 = float(input("x1: "))
y1 = float(input("y1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))
distance = math.dist((x1, y1), (x2, y2))
print(distance)
