# Task:
#   Initialize vector V with 10 values read from keyboard

# ------------------------------------------------------------------------------------------------
# Possible solution using while loop:
values = [0] * 10
index = 0
while index < len(values):
    values[index] = input("Enter text: ")
    index += 1
print(values)

# Possible solution using for-loop:
values = [0] * 10
for index in range(len(values)):
    values[index] = input("Enter text: ")
print(values)

# ------------------------------------------------------------------------------------------------
# Advanced solutions:
# In this case it is actually fine to use `append`:
values = []
for _ in range(10):
    values.append(input("Enter text: "))
    
# A shorter way is to use "list comprehension":
values = [input("Enter text: ") for _ in range(10)]

# ------------------------------------------------------------------------------------------------
# Common mistake:
# 1. The following will read only one number and repeat it 10 times.
values = 10 * [int(input('Enter value: '))]
