# Task: 
#   Show in the console all the elements vector V and their position, each in separate lines.

# ------------------------------------------------------------------------------------------------
# Possible solution using while loop:
values = [4, 8, 15, 16, 23, 42]
index = 0
while index < len(values):
    print(index, values[index])
    index += 1
 
# Possible solution using for loop:
values = [4, 8, 15, 16, 23, 42]
for index in range(len(values)):
    print(index, values[index])
    
# ------------------------------------------------------------------------------------------------
# Advanced solution
# Iterating over both values and indices at the same time is such a frequent task,
# that Python provides a special function `enumerate` for that which can make our life a bit easier:
values = [4, 8, 15, 16, 23, 42]
for index, value in enumerate(values):
    print(index, value)
