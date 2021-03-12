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
