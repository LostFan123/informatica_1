# Task:
#   Write a mini-calculator: a program that reads two numbers and a character. The character
#   must be an arithmetic operation symbol: ‘+', ' -‘, ‘*', ‘/'. The program will show the result of the
#   arithmetic operation between the two numbers.
#   Convierte el ejercicio anterior en un bucle, de forma que se van resolviendo todas las
#   operaciones introducidas por el usuario hasta que éste entre la operacion 0+0, en que el bucle debe
#   acabar.
# Note: for simplicity I will avoid checking for invalid characters from the user input as well as division by zero.

# ------------------------------------------------------------------------------------------------
# Possible solution:
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

# ------------------------------------------------------------------------------------------------
# Common mistakes.
# 1. Using `if` instead of `elif`.
#    While the results will be equivalent, this is not optimal 
#    since it will check the operation against every possible symbol (+-/*),
#    but ideally we can only check it until the match is found
a = float(input("Number 1: "))
op = input("Operation: ")
b = float(input("Number 2: "))
while a != 0 or op != '+' or b != 0:  
    if op == '+': 
        result = a + b
    if op == '-':
        result = a - b
    if op == '*':
        result = a * b
    if op == '/':
        result = a / b
    print(f"{a} {op} {b} = {result}")
    a = float(input("Number 1: "))
    op = input("Operation: ")
    b = float(input("Number 2: "))

# 2. Incorrect check for the "exit" condition can cause problems.
#    Failing example: 2 + (-2)
# 3. Unnecessary initialization of some variables before the loop.
status = True
result = 0  
# the following three variables will get overwritten in any case
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
    print(f"The result of the operation is {result}.")
    status = False if result == 0 and operation == '+' else True
print('Done!')
	
# ------------------------------------------------------------------------------------------------
# Advanced solutions.
# Using `while True` with break:
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
    print(f"{a} {op} {b} = {result}")

# Comparing tuples:
while True:
    a = float(input("Number 1: "))
    op = input("Operation: ")
    b = float(input("Number 2: "))
    if (a, op, b) == (0, '+', 0):
        break
    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    elif op == '*':
        result = a * b
    elif op == '/':
        result = a / b
    print(f"{a} {op} {b} = {result}")
	
# Making a dictionary that will map arithmetic symbols to functions performing the corresponding operations.
# The `operator` library contains several functions that can be used if we want to write arithmetic operations using function calls.
# So, for example, `operator.add(1, 2)` is equivalent to `1 + 2`.
# For dictionaries see here: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
import operator
functions_per_symbol = {'+': operator.add,
                        '-': operator.sub,
                        '*': operator.mul,
                        '/': operator.truediv}
while True:
    a = float(input("Number 1: "))
    op = input("Operation: ")
    b = float(input("Number 2: "))
    if (a, op, b) == (0, '+', 0):
        break
    result = functions_per_symbol[op](a, b)
    print(f"{a} {op} {b} = {result}")
