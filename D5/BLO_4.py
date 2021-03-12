# 1. Try to avoid "hardcoded" values. 
#    Here, 5 is hardcoded and could be replaced by `len(A) - 1`.
# 2. The intent of the `i6 += 5` line can be confusing. 
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
