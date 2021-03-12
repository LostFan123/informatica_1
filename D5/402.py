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
