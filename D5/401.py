# 1. While using `append` in real life is a valid approach, it won't be allowed on the exams:
numbers = []
counter = 0
while counter < 10:
    numbers.append(0)
    counter = counter + 1
print(numbers)

# 2. Defining the list by writing every value is not the best approach:
values = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Solution:
values = [0] * 10
