# 1. This solution violates DRY (Don't repeat yourself) principle. 
#    It is not easily extensible and errorprone. Use loops for these tasks.
v1 = input("Introduce a value:")
v2 = input("Introduce a value:")
v3 = input("Introduce a value:")
v4 = input("Introduce a value:")
v5 = input("Introduce a value:")
v6 = input("Introduce a value:")
v7 = input("Introduce a value:")
v8 = input("Introduce a value:")
v9 = input("Introduce a value:")
v10 = input("Introduce a value:")
V1 = [v1, v2, v3, v4, v5, v6, v7, v8, v8, v9, v10]
print(V1)

# Possible solution using while loop:
values = [0] * 10
index = 0
while index < len(values):
    values[index] = int(input("Enter a number: "))
    index += 1
print(values)

# Possible solution using for-loop:
values = [0] * 10
for index in range(len(values)):
    values[index] = int(input("Enter a number: "))
print(values)
