# 1. Initializing max and min values as zeroes won't work.
#    Failing examples: [1, 2, 3, ...] and [-1, -2, -3, ...]
counter = 0
max_value = 0
min_value = 0
while counter < 5:
    number = float(input("N: "))
    if number > max_value:
        max_value = number
    if number < min_value:
        min_value = number
    counter += 1
print(f"Max: {max_value}")
print(f"Min: {min_value}")


# Possible solution - initialize min and max as the first input:
number = float(input("N: "))
max_value = number
min_value = number
counter = 1
while counter < 5:
    number = float(input("N: "))
    if number > max_value:
        max_value = number
    if number < min_value:
        min_value = number
    counter += 1
print(f"Max: {max_value}")
print(f"Min: {min_value}")
# ^ not optimal as we have duplicated code: `number = float(input("N: "))`

# Alternative solution - use math.inf constants. See: https://docs.python.org/3/library/math.html#math.inf
import math
min_value = math.inf
max_value = -math.inf
counter = 0
while counter < 5:
    number = float(input("N: "))
    if number < min_value:
        min_value = number
    if number > max_value:
        max_value = number
    counter += 1
print(f"Min: {min_value}")
print(f"Max: {max_value}")

# Possible improvements: use `float('inf')`, use `min` and `max` built-in functions:
min_value = float('inf')
max_value = -float('inf')
counter = 0
while counter < 5:
    number = float(input("N: "))
    min_value = min(number, min_value)
    max_value = max(number, max_value)
    counter += 1
print(f"Min: {min_value}")
print(f"Max: {max_value}")
