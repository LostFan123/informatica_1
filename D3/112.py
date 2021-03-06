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

# Same problem. Failing examples: any where operation is not '+', or where any of the operands is zero.
first = int(input("Introduce the first number:"))
second = int(input("Introduce the second number:"))
op = input("Introduce the operator:")
while first != 0 and second != 0 and op == "+":
    if op == "+":
        result = first + second
    elif op == "-":
        result = first - second
    elif op == "*":
        result = first * second
    elif op == "/":
        result = first / second
    print("The solutions is", result)
    first = int(input("Introduce the first number:"))
    second = int(input("Introduce the second number:"))
    op = input("Introduce the character:")
print("Done")

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

# Note: `in` is used to check for an inclusion, `==` is used for equality comparison.
# Here is where we *could* use `in`, though: 
number1 = 1
number2 = 1
symbol = " "
while not (number1 == 0 and number2 == 0 and symbol == '+'):
    print("\n" + "Remember that if you want to go out of the bucle you have to enter the operation 0+0" + "\n")
    number1 = int(input("Write a number: "))
    number2 = int(input("Write a second number: "))
    symbol = " "
    while symbol != "+" and symbol != "-" and symbol != "*" and symbol != "/":  # while symbol not in "+-*/":
        symbol = str(input("Enter a arithmetic operaction symbol (+,-,*,/): "))
    if symbol == "+":
        solution = number1+number2
    elif symbol == "-":
        solution = number1-number2
    elif symbol == "*":
        solution = number1*number2
    else:
        solution = number1/number2
    print("The solution of " + str(number1) + str(symbol) + str(number2) + " is " + str(round(solution)))
