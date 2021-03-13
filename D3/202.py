# Task:
#   Write a program that calculates the sum of 10 numbers entered from keyboard.

# ------------------------------------------------------------------------------------------------
# Possible solution:
counter = 0
total = 0
while counter != 10:
    total += float(input("Number: "))
    counter += 1
print(total)

# If for-loop is allowed:
total = 0
for _ in range(10):  # the underscore is a convention for "throwaway variables"; you can replace it by any other name you want, like `index`
    total += float(input("Number: "))
print(total)

# ------------------------------------------------------------------------------------------------
# Advanced solution:
#   Using `sum` function with a generator expression passed to it as an argument:
print(sum(float(input("Number: ")) for _ in range(10)))
