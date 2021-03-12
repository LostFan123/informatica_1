# Task:
#   Write a program that reads from keyboard 4 numbers and informs if at least two of them are odd

# ------------------------------------------------------------------------------------------------

# Possible solution - create a counter variable:
a = int(input("Number 1: "))
b = int(input("Number 2: "))
c = int(input("Number 3: "))
d = int(input("Number 4: "))
odd_numbers_count = 0
if a % 2 != 0:
    odd_numbers_count += 1  # this is called "augmented assignment" and it's the same as odd_numbers_count = odd_numbers_count + 1
if b % 2 != 0:
    odd_numbers_count += 1
if c % 2 != 0:
    odd_numbers_count += 1
if d % 2 != 0:
    odd_numbers_count += 1
if odd_numbers_count >= 2:
    print("At least two numbers are odd")
else:
    print("Less than two numbers are odd")
    
# Alternatively we can sum the division remainders:
a = int(input("Number 1: "))
b = int(input("Number 2: "))
c = int(input("Number 3: "))
d = int(input("Number 4: "))
if a % 2 + b % 2 + c % 2 + d % 2 >= 2:
    print("At least two numbers are odd")
else:
    print("Less than two numbers are odd")
    
# If the loops are allowed, we can solve it in the following ways.
# Using while loop:
index = 0
odd_numbers_count = 0
while index < 4:
    number = int(input("Number: "))
    if number % 2 != 0:
        odd_numbers_count += 1
if odd_numbers_count >= 2:
    print("At least two numbers are odd")
else:
    print("Less than two numbers are odd")
    
# Using for-loop:
odd_numbers_count = 0
for index in range(4):
    number = int(input("Number: "))
    if number % 2 != 0:
        odd_numbers_count += 1
if odd_numbers_count >= 2:
    print("At least two numbers are odd")
else:
    print("Less than two numbers are odd")
    
# You can see that in the solution above we have a variable `index` that is never used anywhere else.
# For cases like this there is a convention to mark such "throwaway variables" by an underscore (_):
odd_numbers_count = 0
for _ in range(4):
    number = int(input("Number: "))
    if number % 2 != 0:
        odd_numbers_count += 1
if odd_numbers_count >= 2:
    print("At least two numbers are odd")
else:
    print("Less than two numbers are odd")
    
# Also, it is not necessary to check if the number is divisible by two or not.
# We can simply add the remainder of the division. The result will be the same:
odd_numbers_count = 0
for _ in range(4):
    number = int(input("Number: "))
    odd_numbers_count += number % 2
if odd_numbers_count >= 2:
    print("At least two numbers are odd")
else:
    print("Less than two numbers are odd")
 
# ------------------------------------------------------------------------------------------------

# Advanced solution:
#   We can use the built-in `sum` function - https://docs.python.org/3/library/functions.html#sum
#   where the input argument will be a "generator expression":
odd_numbers_count = sum(int(input("Number: ")) % 2 for _ in range(4))
if odd_numbers_count >= 2:
    print("At least two numbers are odd")
else:
    print("Less than two numbers are odd")
    
# In short a generator expression, for example `(x*x for x in range(10))`, 
# is the same as "list comprehension", [x*x for x in range(10)], 
# but where the list is not kept in memory. 
# And a list comprehension is just a shorter way to create lists. So, the example above is roughly equivalent to:
# values = []
# for x in range(10):
#     values.append(x*x)
