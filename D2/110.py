a = int(input("Number 1: "))
b = int(input("Number 2: "))
c = int(input("Number 3: "))
d = int(input("Number 4: "))
odd_numbers_count = 0
if a % 2 != 0:
    odd_numbers_count += 1
if b % 2 != 0:
    odd_numbers_count += 1
if c % 2 != 0:
    odd_numbers_count += 1
if d % 2 != 0:
    odd_numbers_count += 1
if odd_numbers_count >= 2:
    print("At least two numbers are odd")
else:
    print("Less than two numbers are odd")
