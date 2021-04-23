# Task:
#   Write a function media2 that receives two real numbers as arguments, calculates the arithmetic
#   mean of them and then returns the mean as result. Next, write a main program to read two real
#   numbers from keyboard and to call the function to calculate the mean of them.

# ------------------------------------------------------------------------------------------------
# Possible solution:
def media2(a, b):
    return (a + b) / 2

a = float(input("Enter the first real number: "))
b = float(input("Enter the second real number: "))
result = media2(a, b)


# ------------------------------------------------------------------------------------------------
# Advanced solution.
#   It's a good practice to use "type hints" to give a user an idea which kind of data your function
#   should work with, and to let your IDE to warn you if you pass data of some other type.
#   See https://realpython.com/lessons/type-hinting/ for a quick introduction to type hints.
def media2(a: float, b: float) -> float:
    return (a + b) / 2

a = float(input("Enter the first real number: "))
b = float(input("Enter the second real number: "))
result = media2(a, b)
