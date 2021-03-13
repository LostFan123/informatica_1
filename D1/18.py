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
# Common mistakes:
# 1. Writing the code that makes sense in English language, but doesn't make sense in terms of logic of programming language
#    Failing example: 15
number = int(input("Enter a number: "))
if number % 3 and 5 == 0:
    print("YES")
else:
    print("NO")
# Reason: Python follows the precedence table when evaluating the result of an expression.
#   It is similar to the precedence order that we have in math.
#   See: https://docs.python.org/3/reference/expressions.html#operator-precedence
#   Python will evaluate the `number % 3 and 5 == 0` line in the following order:
#   1) `number % 3` (let's denote the result of this operation as A)
#   2) `5 == 0` which will always give `False`
#   3) `A and False` - this will always give `False`. See: https://en.wikipedia.org/wiki/Boolean_algebra#Operations

# ------------------------------------------------------------------------------------------------
# Advanced solution:
#   `if` can actually accept not only boolean values (`True` and `False`), but any values at all.
#   See Python docs on truth value testing: https://docs.python.org/3/library/stdtypes.html#truth-value-testing
#   0 or 0.0 will be considered by `if` as `False`, and any other number will be considered as `True`.
number = int(input("Enter a number: "))
print("NO" if number % 15 else "YES")
