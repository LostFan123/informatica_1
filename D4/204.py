# Task:
#   Write a program that calculates the power xy
#    for 2 numbers entered from keyboard using a
#   loop of products since xy = x*x...*x, up to y-times. Before the loop you should verify that the value
#   of y is positive, otherwise the program will stop..

# ------------------------------------------------------------------------------------------------
# Possible solution:
number = float(input("Number: "))
exponent = int(input("Exponent: "))
if exponent < 0:
    raise ValueError("Exponent must be a positive integer")  # A better alternative to `exit()`
result = 1
counter = 0
while counter < exponent:
    result *= number
    counter += 1
print(f"{number} ** {exponent} == {result}")

# If for-loop is allowed:
number = float(input("Number: "))
exponent = int(input("Exponent: "))
if exponent < 0:
    raise ValueError("Exponent must be a positive integer") 
result = 1
for _ in range(exponent):
    result *= number
print(f"{number} ** {exponent} == {result}")
