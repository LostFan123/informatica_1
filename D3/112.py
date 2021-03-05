# Possible solution:
# Note: we use `elif`s instead of `if`s as we don't need to check the inputted symbol against all possible valid symbols
a = float(input("Number 1: "))
op = input("Operation: ")
b = float(input("Number 2: "))
while a != 0 or op != '+' or b != 0:  # same as `while not (a == 0 and op == '+' and b == 0):`. See: https://en.wikipedia.org/wiki/De_Morgan%27s_laws
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
