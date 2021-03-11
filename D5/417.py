# 1. Using list.index() inside a loop is not optimal 
#    since under the hood it will perform unnecessary search for the value:
values = [4, 8, 15, 16, 23, 42]
for value in values:
    if value % 3 == 0:
        values[values.index(value)] == 0
print(values)

# Possible solution - iterate over indices:
for index in range(len(values)):
    if values[index] % 3 == 0:
        values[index] = 0
print(values)

# Same but using while-loop:
index = 0
while index < len(values):
    if values[index] % 3 == 0:
        values[index] = 0
    index += 1
