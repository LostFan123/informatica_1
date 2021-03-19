# Task:
#   Write a program that reads from keyboard three numbers and determines if the following
#   property meets: one of them is equal to the sum of the other two. For instance numbers 7, 21 y 14
#   meet the condition because 21 = 7+14. The output will be one of these two messages: “Condition is
#   met” or “Condition is not met”.

# ------------------------------------------------------------------------------------------------------
# Solution:
a = float(input("Number 1: "))
b = float(input("Number 2: "))
c = float(input("Number 3: "))
if a == b + c or b == a + c or c == a + b:
    print("Condition is met")
else:
    print("Condition is not met")

# ------------------------------------------------------------------------------------------------------
# Common mistake.
# Repeating yourself:
a = float(input("Number 1: "))
b = float(input("Number 2: "))
c = float(input("Number 3: "))
if  a == b + c:
   print("Condition is met")
elif b == a + c:
   print("Condition is met")
elif c == a + b:
   print("Condition is met")
else:
   print("Condition is not met")
