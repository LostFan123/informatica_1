# Task:
#   Write a program that shows in console all the numbers from 1 to 100 with the following
#   requirements:
#   Show “Fizz” instead of the number if this is multiple of 3.
#   Show “Buzz” instead of the number if this is multiple of 5.
#   Show “FizzBuzz” instead of the number if this is multiple of 3 and 5..

# ------------------------------------------------------------------------------------------------
# Possible solution:
number = 1
while number < 101:
    if number % 15 == 0:  # we can do this a 3 and 5 are coprime numbers
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
    number += 1

# Alternative based on concatenation of strings:
number = 1
while number < 101:
    result = ''
    if number % 3 == 0:
        result += "Fizz"
    if number % 5 == 0:
        result += "Buzz"
    if len(result) == 0:
        result = number
    print(result)
    number += 1
    
# If for-loops are allowed:
for number in range(1, 101):
    result = ''
    if number % 3 == 0:
        result += "Fizz"
    if number % 5 == 0:
        result += "Buzz"
    if len(result) == 0:
        result = number
    print(result)
    
# ------------------------------------------------------------------------------------------------
# Common mistakes:
# 1. Using several if's instead of if-elif will make it check the same number several times
counter = 1
while counter < 101:
    if counter % 3 == 0:
        print("Fizz")
    if counter % 5 == 0:
        print("Buzz")
    if counter % 3 == 0 and counter % 5 == 0:
        print("FizzBuzz")
    else:
        print(counter)
    counter += 1
    
# 2. Performing the same operations is not optimal.
counter = 1
while counter < 101:
    if counter % 3 == 0 and counter % 5 != 0:
        print("Fizz")
        counter += 1  # <- this line is also repeated 4 times but could be taken out
    if counter % 3 != 0 and counter % 5 == 0:
        print("Buzz")
        counter += 1
    if counter % 3 == 0 and counter % 5 == 0:
        print("FizzBuzz")
        counter += 1
    else:
        print(counter)
        counter += 1
        
# ------------------------------------------------------------------------------------------------
# Advanced solution:
#   Using the fact that `A or B` where `A` and `B` are not necessarily booleans, will return the first
#   true-like value, where false-like (or falsy) values are 0, 0.0, [], ''.
for number in range(1, 101):
    result = ''
    if number % 3 == 0:
        result += "Fizz"
    if number % 5 == 0:
        result += "Buzz"
    print(result or number)
