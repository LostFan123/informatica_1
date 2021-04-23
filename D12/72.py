# Task:
#   Write the function imprimir which receives as parameter a vector of numbers and shows in
#   console each one of the elements of the vector together with its position in the vector

# ------------------------------------------------------------------------------------------
# Possible solution.
# Since you've already passed the mid-term exam, I think it's safe to use the built-in
# `enumerate` function: https://docs.python.org/3/library/functions.html#enumerate
# See also: https://stackoverflow.com/questions/522563/accessing-the-index-in-for-loops
def imprimir(numbers):
    for index, number in enumerate(numbers):
        print(index, number)
        
# Example of usage:
imprimir([4, 8, 15, 16, 23, 42])

        
# ------------------------------------------------------------------------------------------
# Advanced solution.
# Using type hints:
from typing import List  # unnecessary in Python >= 3.9, use simple `list` instead

def imprimir(numbers: List[float]) -> None:
    for index, number in enumerate(numbers):
        print(index, number)
