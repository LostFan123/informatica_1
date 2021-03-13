# Task:
#   A vector A contains sorted values which correspond to the limits of several age intervals:
#   For example: A=[25, 40, 65, 80] establishes 5 intervals: (1st) up to 24, (2nd) from 25 to 39, (3rd)
#   from 40 to 64, (4th) from 65 to 79, and (5th) from 80 on.
#   A second vector, KC contains the values of the recommended Kcal that a person should burn
#   depending on the age interval.
#   Write the code which asks the user for his/her age and responds with the recommended maximum
#   Kcal.
#   EXAMPLE: If A=[25, 40, 65, 80] and KC=[120, 110, 105, 100, 90 ], for a 42-years old person the
#   response should be 105 Kcal.

# ------------------------------------------------------------------------------------------------
# Possible solution:
age = int(input("Enter your age: "))
A = [25, 40, 65, 80]
KC = [120, 110, 105, 100, 90]
counter = 0
is_age_found = False
while counter < len(A) and not is_age_found:
    if A[counter] > age:
        is_age_found = True
    else:
        counter += 1
print(KC[counter]))

# ------------------------------------------------------------------------------------------------
# Advanced solutions:
# Using for-else loop construct 
user_age = int(input("Enter your age: "))
A = [25, 40, 65, 80]
KC = [120, 110, 105, 100, 90]
for index, age in enumerate(A):
    if age > user_age:
        break
else:
    index += 1
print(KC[index])

# Alternatively using `bisect_right` function.
# This will search for an index of the first value in a list which is less or equal than the given value.
# See: https://docs.python.org/3/library/bisect.html#bisect.bisect_left
from bisect import bisect_right
age = int(input("Enter your age: "))
A = [25, 40, 65, 80]
KC = [120, 110, 105, 100, 90]
index = bisect_right(A, age)
print(KC[index])
    
# ------------------------------------------------------------------------------------------------
# Common mistakes:
# 1. Not the most optimal approach.
#    It is not extensible - try adding more age ranges and corresponding calories values, and you will have to add more `elif` cases.
#    Instead you can use for/while loops.
A = [25, 40, 65, 80]
KC = [120, 110, 105, 100, 90]
age = int(input("Introduce your age: "))
if age < A[0]:
    print(str(KC[0]))
elif age < A[1] and age >= A[0]:
    print(str(KC[1]))
elif age < A[2] and age >= A[1]:
    print(str(KC[2]))
elif age < A[3] and age >= A[2]:
    print(str(KC[3]))
else:
    print(str(KC[4]))

# 2. Try to avoid "hardcoded" values. 
#    Here, 5 is hardcoded and could be replaced by `len(A) - 1`.
# 3. The intent of the `i6 += 5` line can be confusing. 
#    Use flag variable or `break` statement instead.
A = [25, 40, 65, 80]
KC = [120, 110, 105, 100, 90]
age = eval(input("Introduce the age:"))
i6 = 0
while i6 < 5:
    if A[i6] > age:
        print("The Kcal should be", KC[i6])
        i6 += 5
    elif age > 80:
        print("The Kcal shouldn't be above 90")
        i6 += 5
    else:
        i6 += 1
