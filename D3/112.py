# 1. Incorrect check for the "exit" condition can cause problems.
#    Failing example: 2 + (-2)
# 2. Unnecessary initialization of some variables before the loop.
status = True
result = 0
left_operand = 0
right_operand = 0
operation = ''
while status:
    operation = input("Operation: ")
    left_operand = int(input("Enter a number: "))
    right_operand = int(input("Entry a second number: "))
    if operation == '+':
        result = left_operand + right_operand
    elif operation == '-':
        result = left_operand - right_operand
    elif operation == '*':
        result = left_operand * right_operand
    elif operation == '/':
        result = left_operand / right_operand
    else:
        print("You haven't selected an operation")  # here we should also stop the current iteration
    print(f"The result of the operation is {result}.")
    status = False if result == 0 and operation == '+' else True
print('Done!')

# Possible solution:
# Note: we use `elif`s instead of `if`s as we don't need to check the inputted symbol against all possible valid symbols
a = float(input("Number 1: "))
op = input("Operation: ")
b = float(input("Number 2: "))
while a != 0 or op != '+' or b != 0:  # same as `while not (a == 0 and op == '+' and b == 0):`. See: https://en.wikipedia.org/wiki/De_Morgan%27s_laws
    if op == '+':  # `if '+' in op:` will check a presence of '+' character in the string `op`
        result = a + b
    elif op == '-':
        result = a - b
    elif op == '*':
        result = a * b
    elif op == '/':
        result = a / b
    print(f"{a} {op} {b} = {result}")
    a = float(input("Number 1: "))
    op = input("Operation: ")
    b = float(input("Number 2: "))

# or using `while True` with break:
while True:
    a = float(input("Number 1: "))
    op = input("Operation: ")
    b = float(input("Number 2: "))
    if a == 0 and op == '+' and b == 0:
        break
    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    elif op == '*':
        result = a * b
    elif op == '/':
        result = a / b
    else:
        print(f"Invalid operation '{op}'. Try again.")
    print(f"{a} {op} {b} = {result}")

# One of the solutions I've received used string comparisons:
print("To exit the program you must write the following operation : 0+0 .")
n1 = int(input("Enter the first number: "))
op = str(input("Enter operation ( + , - , / , * ) : "))
n2 = int(input("Enter the second number: "))
total = str(n1) + op + str(n2)
while total != "0+0":
	if op == "+":
		print("The result is " , n1 + n2 , ".")
	elif op == "-":
		print("The result is " , n1 - n2 , ".")
	elif op == "/":
		print("The result is " , n1 / n2 , ".")
	elif op == "*":
		print("The result is " , n1 * n2 , ".")
	else:
		print("The operation must be + or - or * or /.")
	n1 = int(input("Enter another number: "))
	op = str(input("Enter operation ( + , - , / , * ) : "))
	n2 = int(input("Enter another number: "))
	total = str(n1) + op + str(n2) 
# a simpler way to write this condtion will be `while (n1, op, n2) != (0, '+', 0):`
