# Task:
#   Determine if all the numbers of a sequence of numbers read from keyboard and finished in
#   0 are even. 

# ------------------------------------------------------------------------------------------------
# Possible solution:
are_all_even = True
number = 1  # just some default value to enter the loop
while number != 0:
    number = int(input("N: "))
    if number % 2 != 0:
        are_all_even = False
if are_all_even:
    print("All numbers are even")
else:
    print("Not all numbers are even")

# ------------------------------------------------------------------------------------------------
# Advanced solution.
# Using `while True` with `break`:
are_all_even = True
while True:
    number = int(input("N: "))
    if number == 0:
        break
    if number % 2 != 0:
        are_all_even = False
if are_all_even:
    print("All numbers are even")
else:
    print("Not all numbers are even")
