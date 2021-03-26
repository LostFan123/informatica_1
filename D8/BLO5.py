# Task:
#   We have an array VEG which contains the months in which a list of vegetables can be plant. Each
#   row has the information of a vegetable and columns (2) contains the first and last month in which
#   that vegetable can be planted. Write a program that ask the user for a vegetable row number and its
#   name and shows a plot of the months when this vegetables can be planted

# -----------------------------------------------------------------------------------------------------
# Solution:
import matplotlib.pyplot as plt

VEG = [[2,5], [4,6], [1,7], [8,8], [4,5], [1,12], [10,11]]
row_number = int(input("Enter vegetable -number of row- : "))
name = input("Enter vegetable -name- : ")
months = range(1, 13)  # 1, 2, ..., 12
counters = [0] * 12
month = VEG[row_number][0]
while month <= VEG[row_number][1]:
    counters[month] = 1
    month += 1
plt.bar(months, counters)
plt.title(name)

# -----------------------------------------------------------------------------------------------------
# Advanced solution.
# Using list slicing to reassing a chunk of values to 1s at once
import matplotlib.pyplot as plt

VEG = [[2,5], [4,6], [1,7], [8,8], [4,5], [1,12], [10,11]]
row_number = int(input("Enter vegetable -number of row- : "))
name = input("Enter vegetable -name- : ")
counters = [0] * 12
first, last = VEG[row_number]
counters[first:last + 1] = [1] * (last + 1 - first)
plt.bar(range(1, 13), counters)
plt.title(name)
