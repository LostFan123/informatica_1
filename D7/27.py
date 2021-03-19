# Task:
#   Write a program that given a positive number informs which is its greater prime digit. For
#   instance, if the number is 1472 the program will return the digit 7.

# ------------------------------------------------------------------------------------------------
# Possible solution:
number = int(input("N: "))
largest_prime_digit = 0
while number != 0:
    number, digit = divmod(number, 10)
    if (digit == 2 or digit == 3 or digit == 5 or digit == 7) and digit > largest_prime_digit:
        largest_prime_digit = digit
if largest_prime_digit == 0:
    print("No prime numbers were found")
else:
    print(largest_prime_digit)
    
# ------------------------------------------------------------------------------------------------
# Advanced solution.
# Using `max` built-in function with `default` parameter: https://docs.python.org/3/library/functions.html#max
number = input("N: ")  # reading a number as string in order to iterate over characters
primes = {'2', '3', '5', '7'}  # a set of prime digits as strings: https://docs.python.org/3/tutorial/datastructures.html#sets
print(max((digit for digit in number if digit in primes),  # using a generator expression: https://stackoverflow.com/questions/47789/generator-expressions-vs-list-comprehensions
           default="No prime numbers were found"))
        
