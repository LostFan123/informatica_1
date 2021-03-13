# Task:
#   Determine if all the digits of number n are even. 
    
# ------------------------------------------------------------------------------------------------
# Possible solution:
number = int(input("Number: "))
all_digits_are_even = True
while number != 0 and all_digits_are_even:
    number, digit = divmod(number, 10)
    if digit % 2 != 0:
        all_digits_are_even = False
if all_digits_are_even:
    print("All digits are even.")
else:
    print("Not all digits are even.")
    
# ------------------------------------------------------------------------------------------------
# Advanced solutions:
#   Treating a number as a string and using the for-else loop construct.
number = input("Enter a number: ")
for digit in number:
    if int(digit) % 2 != 0:
        print("Not all digits are even.")
else:
    print("There are no 2 even digits")
    
# Alternatively we can use the built-in `all` function with a generator expression.
# The `all` function will check if all the items of the received iterable are evaluated as `True`.
# See: https://docs.python.org/3/library/functions.html#all
# To check if a digit is even we can make a set, https://docs.python.org/3/tutorial/datastructures.html#sets 
# of all even digits in advance. 

number = input("Enter a number: ")
all_digits_are_even = all(digit in even_digits for digit in number)  # `digit in even_digits` will return `True` or `False`
if all_digits_are_even:
    print("All digits are even.")
else:
    print("Not all digits are even.")
    
# Yet another approach is to convert the input number to a set of characters 
# and check if the difference of this set with the set of all even digits is empty or not:
even_digits = {'0', '2', '4', '6', '8'}
if set(input("Enter a number: ")) - even_digits:  # will be evaluated as `False` only if the difference of these sets is empty
    print("All digits are even.")
else:
    print("Not all digits are even.")
    
