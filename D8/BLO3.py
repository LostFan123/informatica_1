# Task:
#   Write a program that reads a sequence of numbers from keyboard, finished with 0, and shows the
#   two first numbers that are multiple of 2 and greater 21. For example, entering the sequence 23, 48,
#   5, -6, 41, 990, ... the program will show the numbers 48 and 990 and will stop immediately after
#   showing 990.

# -----------------------------------------------------------------------------------------------------
# Solution:
found_numbers_count = 0
is_sequence_ended = False
while found_numbers_count < 2 and not is_sequence_ended:
    number = int(input("Enter a number (0 to finish): "))
    if number == 0:
        is_sequence_ended = True
    elif number > 21 and number % 2 == 0:
        found_numbers_count += 1
        print(number)

# -----------------------------------------------------------------------------------------------------
# Advanced solution.
# Using `break`
found_numbers_count = 0
while found_numbers_count < 2:
    number = int(input("Enter a number (0 to finish): "))
    if number == 0:
        break
    if number > 21 and number % 2 == 0:
        found_numbers_count += 1
        print(number)
