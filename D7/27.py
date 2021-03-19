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
# Common mistakes.
# 1. Iterating over the digits of the number 9 times at worst instead of once
number = int(input("Enter a number "))
digit = 9
while digit != 0:
    if str(digit) in str(number):  # implicit iteration over the string is here
        print(digit)
        digit = 0
    else:
        digit -= 1
        
# 2a. Incorrect condition.
#     Failing example: 23
number = int(input("Please write a number: "))
i = 0
maximum = 0
while number != 0:
    div = number % 10
    if maximum < div and div % 2 != 0 and div % 3 != 0:  # won't catch 2 or 3
        maximum = div
    else:
        maximum = maximum  # this line is useless
    i += 1
    number = number // 10
print("The greater prime digit is " + str(maximum))
# 2b. Another example of incorrect condition.
#     Failing example: 34
number = str(input("Enter a number: "))
lista = [7,5,3,2]
greater_prime_digit = 0
for digit in number:
    for x in lista:
        if int(digit) % x == 0 and greater_prime_digit < int(digit):  # first condition will match 4,6,8,9
            greater_prime_digit = int(digit)
print(greater_prime_digit)
    
# ------------------------------------------------------------------------------------------------
# Advanced solution.
# Using `max` built-in function with `default` parameter: https://docs.python.org/3/library/functions.html#max
number = input("N: ")  # reading a number as string in order to iterate over characters
primes = {'2', '3', '5', '7'}  # a set of prime digits as strings: https://docs.python.org/3/tutorial/datastructures.html#sets
print(max((digit for digit in number if digit in primes),  # using a generator expression: https://stackoverflow.com/questions/47789/generator-expressions-vs-list-comprehensions
           default="No prime numbers were found"))    
