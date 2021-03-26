# Task:
#   Write a program that reads from the keyboard a number and calculates the summation of the digits
#   in odd positions. Assume that digit positions start from right to left. For instance, for the number
#   49263 the digit in position 1 is digit 3, and the summation of the digits in odd positions is 3+2+4=9.

# ---------------------------------------------------------------------------------------------------------
# Solution:
number = int(input("N: "))
odd_digits_sum = 0
while number > 0:
    number, digit = divmod(number, 10)
    odd_digits_sum += digit
    number //= 10
print(odd_digits_sum)

# ---------------------------------------------------------------------------------------------------------
# Advanced solution.
# Using string slicing and built-in `sum` function with a generator expression as input argument:
number = input("N: ")
print(sum(int(digit) for digit in number[::-2]))
