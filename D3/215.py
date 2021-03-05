# 1. Using several if's instead of if-elif will make it check the same number several times
counter = 1
while counter < 21:
    if counter % 3 == 0:
        print("Fizz")
    if counter % 5 == 0:
        print("Buzz")
    if counter % 3 == 0 and counter % 5 == 0:
        print("FizzBuzz")
    else:
        print(counter)
    counter += 1

# Possible solution:
number = 1
while number < 101:
    if number % 15 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
    number += 1
