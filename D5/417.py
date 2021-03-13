# Task:
#   Write the code to eliminate from the array V=[12, 3, 4, 65, 23, 81, 43, 9] all the values that are
#   multiple of 3. Change their value to 0. Finally, show the all the values of the vector in the console.

# ------------------------------------------------------------------------------------------------
# Possible solution using while loop
values = [12, 3, 4, 65, 23, 81, 43, 9]
index = 0
while index < len(values):
    if values[index] % 3 == 0:
        values[index] = 0
    index += 1
    
# And using for-loop
values = [12, 3, 4, 65, 23, 81, 43, 9]
for index in range(len(values)):
    if values[index] % 3 == 0:
        values[index] = 0
print(values)

# ------------------------------------------------------------------------------------------------
# Advanced solution
# Using list comprehension with conditional expression:
values = [12, 3, 4, 65, 23, 81, 43, 9]
values = [value if value % 3 != 0 else 0 for value in values]
print(values)

# ------------------------------------------------------------------------------------------------
# Common mistakes:
# 1. Using list.index() inside a loop is not optimal 
#    since under the hood it will perform unnecessary search for the value:
values = [4, 8, 15, 16, 23, 42]
for value in values:
    if value % 3 == 0:
        values[values.index(value)] == 0
print(values)

# 2. Simply printing zeros won't do. The task asks us to update the list:
values = [12, 3, 4, 65, 23, 81, 43, 9]
for value in values:
   if value % 3 == 0:
       value = 0
   print(value)

