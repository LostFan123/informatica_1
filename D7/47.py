# Task:
#   Assume you have a vector such as V=[3, 5, 7, 4, 6, 2, 8, 14, 23, 4]
#   Write the program that determines the position of the first number preceded by a multiple of 7
#   (For simplicity let's also assume that the first number is never a multiple of 7, 
#    and there will be always at least one multiple of 7 in the list)

# ------------------------------------------------------------------------------------------------
# Solution:
V = [3, 5, 7, 4, 6, 2, 8, 14, 23, 4]
index = 1  # we can start from the second element
found = False
while index < len(V) and not found:
    if V[index] % 7 == 0:
        found = True
    index += 1
print(index - 2)  # taking into account that when the number is found we still add +1 to it

# ------------------------------------------------------------------------------------------------
# Advanced solutions.
# Using `while True` with `break`:
V = [3, 5, 7, 4, 6, 2, 8, 14, 23, 4]
index = 1
while True:
    if V[index] % 7 == 0:
        break
    index += 1
print(index - 1)

# Using `enumerate`, https://stackoverflow.com/questions/522563/accessing-the-index-in-for-loops
for index, number in enumerate(V):
    if number % 7 == 0:
        break
print(index - 1)

# Using `next`:
# See: https://stackoverflow.com/questions/1701211/python-return-the-index-of-the-first-element-of-a-list-which-makes-a-passed-fun
V = [3, 5, 7, 4, 6, 2, 8, 14, 23, 4]
divisible_index = next(index for index, number in enumerate(V) if number % 7 == 0)
print(divisible_index - 1)
