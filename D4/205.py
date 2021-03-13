# Task:
#   Write a program that counts the number of digits of a positive integer number X introduced
#   from keyboard. Use a loop that divides X by 10 successively until 0. 

# ------------------------------------------------------------------------------------------------
# Solution:
number = int(input("Number: "))
digits_count = 0
while number != 0:
    number = number // 10
    digits_count += 1
print(digits_count)

# Alternatively using `while True:` with `break`:
number = int(input("Number: "))
digits_count = 0
while True:
    if number == 0:  # or `if not number:`
        break
    number = number // 10
    digits_count += 1
print(digits_count)
