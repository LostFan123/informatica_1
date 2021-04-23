# Task:
#   Write a function to receive an integer number as an argument. Reverse all digits of the original
#   number: for example, if the function receives the number 356, it will return the number 653. Return
#   the result to the main program.
#   Note: assuming that we have to return an integer as well, so `10` would return `1`.

# -----------------------------------------------------------------------------------------------------
# Possible solution:
#   Converting a number to string, reversing the characters, and converting the resulting string
#   back to integer.
#   See: https://stackoverflow.com/questions/931092/reverse-a-string-in-python
#   and: https://stackoverflow.com/questions/509211/understanding-slice-notation
def reverse(number):
    return int(str(number)[::-1])

# Usage example:
print(reverse(123))  # will print `321`


# -----------------------------------------------------------------------------------------------------
# Advanced solution.
# Using type hints:
def reverse(number: int) -> int:
    return int(str(number)[::-1])
