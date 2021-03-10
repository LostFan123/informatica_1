# 1. Logical mistake. All digits != any digits:
number = int(input("Number: "))
even_digits_count = 0
while number != 0:
    digit = number % 10
    number = number // 10
    print(digit)
    if digit % 2 == 0:
        even_digits_count += 1
    elif digit == 0:
        even_digits_count += 1
print("Number of even digits:", even_digits_count)
if even_digits_count != 0:
    print("All digits are even.")
else:
    print("No digits are even.")
    
# 2. Using not intended tools probably won't be accepted on exams...
x = float(input("Enter a number ")) 
if "1" in str(x):
    print("Not all digits are even numbers")
elif "3" in str(x):
    print("Not all digits are even numbers")
elif "5" in str(x):
    print("Not all digits are even numbers")
elif "7" in str(x):
    print("Not all digits are even numbers")
elif "9" in str(x):
    print("Not all digits are even numbers")
else:
    print("All digits are even numbers")
    
# Possible solution:
number = int(input("Number: "))
all_digits_are_even = True
while number != 0 and all_digits_are_even:
    number, digit = divmod(number, 10)
    if digit % 2 != 0:
        all_digits_are_even = False
if all_digits_are_even != 0:
    print("All digits are even.")
else:
    print("Not all digits are even.")
