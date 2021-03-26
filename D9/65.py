# Task:
#   A) Create a program that read a sequence of numbers from a file and writes the sum and the mean
#      of them in console. Do not use a vector to do it !
#   B) Extend your program 1 to calculate and show also the standard deviation. Now, can you do this
#      without a vector?
# Note: assuming that numbers are written in the file line by line

# --------------------------------------------------------------------------------------------------
# Possible solution for A):
# Using file.close()
file = open('numbers.txt')
total = 0
numbers_count = 0
for number in file:
    total += float(number)
    numbers_count += 1
print(f"Sum: {total}")
print(f"Mean: {total / numbers_count}")
file.close()

# Using `with`:
with open('numbers.txt') as file:
    total = 0
    numbers_count = 0
    for number in file:
        total += float(number)
        numbers_count += 1
print(f"Sum: {total}")
print(f"Mean: {total / numbers_count}")

# Possible solution for B):
# Keeping the data in the list:
with open('numbers.txt') as file:
    numbers = list(file)  # or `file.readlines()`
total = 0
for number in numbers:
    total += float(number)
mean = total / len(numbers)
numerator = 0
for number in numbers:
    numerator += (float(number) - mean) ** 2
stdev = (numerator / len(numbers)) ** 0.5
print(f"Sum: {total}")
print(f"Mean: {mean}")
print(f"Standrad deviation: {stdev}")

# Avoiding list by iterating over the file twice:
with open('numbers.txt') as file:
    total = 0
    numbers_count = 0
    for number in file:
        total += float(number)
        numbers_count += 1
mean = total / len(numbers_count)
with open('numbers.txt') as file:
    numerator = 0
    for number in file:
        numerator += (float(number) - mean) ** 2
stdev = (numerator / numbers_count) ** 0.5
print(f"Sum: {total}")
print(f"Mean: {mean}")
print(f"Standrad deviation: {stdev}")

# --------------------------------------------------------------------------------------------------
# Advanced solution for A).
# Delegate counting to `enumerate`:
with open('numbers.txt') as file:
    total = 0
    for line_number, number in enumerate(file, start=1):
        total += float(number)
print(f"Sum: {total}")
print(f"Mean: {total / line_number}")

# Advanced solution for B).
# Using `statistics` library: https://docs.python.org/3/library/statistics.html
# and `map` to apply `float` function to each line of the file - more concise way
# of writing the loop.
from statistics import mean, stdev

with open('numbers.txt') as file:
    numbers = list(map(float, file))
print(f"Sum: {sum(numbers)}")
print(f"Mean: {mean(numbers)}")
print(f"Standrad deviation: {stdev(numbers)}")
