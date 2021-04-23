# Task:
#   Write a program that calculates p the number of total possible combinations of i elements from a
#   list of n elements. The expression to calculate p is:
#   p=n!/(i!(n−i)!)
#   Define first a function calcula_factorial to calculate the factorial of any given number. Then use
#   this function to calculate p. The values of n and i are entered from keyboard. The function shall
#   verify that n is a positive integer number and that i is also a positive integer number within [0-n]. 


# -------------------------------------------------------------------------------------------------------
# Possible solutions:
def calcula_factorial(number):
    factorial = 1
    while number > 1:
        factorial = factorial * number  # or `factorial *= number`
        number -= 1
    return factorial


def combination(n, i):
    if n < 1:
        raise ValueError(f"Expected a positive `n`, got {n} instead.")
    if i < 0:
        raise ValueError(f"Expected a positive `i`, got {i} instead.")
    if i > n:
        return 0  # according to definition
    return calcula_factorial(n) / (calcula_factorial(i) * calcula_factorial(n - i))

n = int(input("n: "))
i = int(input("i: "))
result = combination(n, i)

# Alternatively we can use `for` loop for calculating factorial:
def calcula_factorial(number):
    factorial = 1
    for value in range(1, number + 1):
        factorial *= value
    return factorial

# -------------------------------------------------------------------------------------------------------
# Advanced solution.
#   Ignoring the fact that both functions already exist in Python: 
#   combination - https://docs.python.org/3/library/math.html#math.comb
#   factorial - https://docs.python.org/3/library/math.html#math.factorial
#   1. Using type hints.
#   2. Using functools.reduce together with operator.mul to calculate the factorial. 
#      See: https://docs.python.org/3/library/functools.html#functools.reduce
#   3. Adding docstring to `combination` function to explain what it is supposed to do.
#      See: https://realpython.com/documenting-python-code/
import operator
from functools import reduce

def calcula_factorial(number: int) -> int:
    return reduce(operator.mul, range(2, number + 1), 1)

def combination(n: int, i: int) -> int:
    """
    Return the number of ways to choose `i` items from `n` items 
    without repetition and without order.
    """
    if n < 1:
        raise ValueError(f"Expected a positive `n`, got {n} instead.")
    if i < 0:
        raise ValueError(f"Expected a positive `i`, got {i} instead.")
    if i > n:
        return 0
    return calcula_factorial(n) / (calcula_factorial(i) * calcula_factorial(n - i))
