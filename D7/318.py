# Task:
#   Determine if number n meets the following property: the sum of its digits is less or equal 100
#   and none of them are 5

# ------------------------------------------------------------------------------------------------
# Solution:
number = int(input("N: "))
meets_properties = True
digits_sum = 0
while number != 0 and meets_properties:
    number, digit = divmod(number, 10)
    digits_sum += digit
    if digit == 5 or digits_sum > 100:
        meets_properties = False
if meets_properties:
    print("Number meets the properties")
else:
    print("Number doesn't meet the properties")
    
# ------------------------------------------------------------------------------------------------
# Advanced solution.
# Using for-else loop construct with `break`
number = input("N: ")
digits_sum = 0
for char in number:
    digit = int(char)
    digits_sum += digit
    if digit == 5 or digits_sum > 100:
        print("Number doesn't meet the properties")
        break
else:
    print("Number meets the properties")
