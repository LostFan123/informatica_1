# Task:
#   Write the function buscar_max which receives as parameter a vector of numbers and returns as
#   output parameter the index of the greatest element inside the vector. Don’t use the builtin function
#   max()

# ------------------------------------------------------------------------------------------------------
# Possible solution:
def buscar_max(numbers):
    if not numbers:  # https://stackoverflow.com/questions/53513/how-do-i-check-if-a-list-is-empty
        raise ValueError("Cannot find maximum in an empty list.")
    maximum = -float("inf")
    for index, number in enumerate(numbers):
        if number > maximum:
            maximum = number
            maximum_index = index
    return maximum_index

# Usage example:
index = buscar_max([3, 4, 2])


# ------------------------------------------------------------------------------------------------------
# Advanced solution.
#   Just adding the type hints.
from typing import List  # unnecessary in Python >= 3.9, just use built-in `list`

def buscar_max(numbers: List[float]) -> int:
    if not numbers: 
        raise ValueError("Cannot find maximum in an empty list.")
    maximum = -float("inf")
    for index, number in enumerate(numbers):
        if number > maximum:
            maximum = number
            maximum_index = index
    return maximum_index

# If `max` would've been allowed, we could do:
def buscar_max(numbers: List[float]) -> int:
    if not numbers:  
        raise ValueError("Cannot find maximum in an empty list.")
    return max((number, index) for index, number in enumerate(numbers))[1]
# or using `itemgetter` as a key: https://docs.python.org/3/library/operator.html#operator.itemgetter
from operator import itemgetter

def buscar_max(numbers: List[float]) -> int:
    if not numbers:  
        raise ValueError("Cannot find maximum in an empty list.")
    return max(enumerate(numbers), key=itemgetter(1))[0]

# or the same approach but using `lambda`:
# https://realpython.com/python-lambda/
# https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions
def buscar_max(numbers: List[float]) -> int:
    if not numbers:  
        raise ValueError("Cannot find maximum in an empty list.")
    return max(enumerate(numbers), key=lambda x: x[1])[0]

# using `__getitem__` "dunder" method. Where dunder means double-underscore.
# For now you can think of this method as another way to get an item from a list
# by index:
# `first = my_list[0]` is equivalent to `first = my_list.__getitem__(0)`.
# And in the following case the key `numbers.__getitem__` is a function that
# for a given index will return the corresponding value in `numbers`.
def buscar_max(numbers: List[float]) -> int:
    if not numbers:  
        raise ValueError("Cannot find maximum in an empty list.")
    return max(range(len(numbers)), key=numbers.__getitem__)
