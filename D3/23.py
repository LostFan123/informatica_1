import math
minimum = math.inf
maximum = -math.inf
counter = 0
while counter != 20:
    number = float(input("Number: "))
    if number < minimum:
        minimum = number
    if number > maximum:
        maximum = number
    counter += 1
print(f"Min: {minimum}")
print(f"Max: {maximum}")

# or using `min` and `max` built-in functions:
import math
minimum = math.inf
maximum = -math.inf
counter = 0
while counter != 20:
    number = float(input("Number: "))
    minimum = min(number, minimum)
    maximum = max(number, maximum)
    counter += 1
print(f"Min: {minimum}")
print(f"Max: {maximum}")
