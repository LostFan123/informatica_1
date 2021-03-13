# Task:
#   Write a program that reads form keyboard two numbers and dispays a message “YES” if at
#   least one of the two numbers are divisible by 7. The output must be “NO” if the condition is not
#   met.

# ------------------------------------------------------------------------------------------------
# Solution:
first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
if first % 7 == 0 or second % 7 == 0:
    print("YES")
else:
    print("NO")
    
