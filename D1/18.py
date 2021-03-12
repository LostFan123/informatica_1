# Task:
#   Write a program that reads form keyboard a number and dispays a message “YES” if the
#   number is multiple of 5 and 3 at the same time. The output must be “NO” if the condition is not
#   met.

# ------------------------------------------------------------------------------------------------

# Solution:
number = int(input("Enter a number: "))
if number % 3 == 0 and number % 5 == 0:
    print("YES")
else:
    print("NO")
    
# Alternatively, taking into account that 3 and 5 are coprime numbers:
number = int(input("Enter a number: "))
if number % 15 == 0:
    print("YES")
else:
    print("NO")
    
# This can be also shortened by using a "conditional expression":
number = int(input("Enter a number: "))
print("YES" if number % 15 == 0 else "NO")

# ------------------------------------------------------------------------------------------------

# Advanced solution:
#   `if` can actually accept not only boolean values (`True` and `False`), but any values at all.
#   See Python docs on truth value testing: https://docs.python.org/3/library/stdtypes.html#truth-value-testing
#   0 or 0.0 will be considered by `if` as `False`, and any other numbers will be considered as `True`.
number = int(input("Enter a number: "))
print("NO" if number % 15 else "YES")
