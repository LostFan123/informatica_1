number = int(input("Number: "))
digits_count = 0
while number != 0:
    number = number // 10
    digits_count += 1
print(digits_count)
