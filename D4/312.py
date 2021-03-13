# Task:
#   Determine if the number n has 2 or more even digits

# ------------------------------------------------------------------------------------------------
# Possible solution:
number = int(input("Enter a number: "))
counter = 0
while counter < 2 and number != 0:
    number, digit = divmod(number, 10)
    if digit % 2 == 0:
        counter = counter + 1
if counter == 2:
    print("There are at least 2 even digits")
else:
    print("There are no 2 even digits")
    
# ------------------------------------------------------------------------------------------------
# Advanced solutions:
#   Treating a number as a string and using the for-else loop construct.
number = input("Enter a number: ")
counter = 0
for digit in number:
    if int(digit) % 2 == 0:
        counter = counter + 1
    if counter == 2:
        print("There are at least 2 even digits")
        break
else:
    print("There are no 2 even digits")
    
# Alternatively we can use `sum` function with a generator expression.
# To check if a digit is even we can make a set, https://docs.python.org/3/tutorial/datastructures.html#sets 
# of all even digits in advance. 
# We will also use the fact that we can add booelans together: `True + True == 2`
even_digits = {'0', '2', '4', '6', '8'}
number = input("Enter a number: ")
even_digits_count = sum(digit in even_digits for digit in number)  # `digit in even_digits` will return `True` or `False`
if even_digits_count >= 2:
    print("There are at least 2 even digits")
else:
    print("There are no 2 even digits")
    
# ------------------------------------------------------------------------------------------------
# Common mistales:
# 1. Unnecessary counting of odd digits.
# 2. Incorrect order of calculating quotient and remainder - n gets overwritten before we get the first digit.
#    Failing example: 21
n = int(input("Tell me a number: "))
even = 0
odd = 0
while (n>0):
    n = n//10
    if ((n%10)%2 == 0):
        even = even + 1
    else: 
        odd = odd + 1
if (even == 2):
    print("This number has 2 even digits")
elif (even > 2):
    print("This number has more than 2 even digits")
else:
    print("This number has no even digits")


