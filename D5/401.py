# Task:
#   Initialize vector V with 10 zeros

# ------------------------------------------------------------------------------------------------
# Solution:
values = [0] * 10

# ------------------------------------------------------------------------------------------------
# Common mistakes:
# 1. Not only using `append` won't be allowed on the exams. This is also both a slower and more verbose approach.
numbers = []
counter = 0
while counter < 10:
    numbers.append(0)
    counter = counter + 1
print(numbers)

# 2. Defining the list by writing every value is more difficult to read and not extensible in case if we want to change 10 to some other number:
values = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

