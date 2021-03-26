# Task:
#   Having a text file with the name expresiones.txt in which each line has an arithmetic expression
#   such as:
#   <operator> <operand1> <operand2>
#   possible operators are characters ‘+', ‘-‘, ‘x', '/' and ‘%' and operands 1 and 2 are integer
#   numbers. For example:
#   * 34 2
#   Write the program that creates a new file calculos.txt to hold the results of each arithmetic
#   expression of the first file. The format of the output file should be:
#   <operand1> <operator> <operand2> = <result>
#   For example:
#   34 * 2 = 68
#   The program should also write the adequate error messages for each one of the following cases:
#    Unable to find or read the input file expresiones.txt
#    Unable to create or write the output file calculos.txt
#    The arithmetic expression of one line of file expresiones.txt does not follow the established
#   format. 

# -------------------------------------------------------------------------------------------------
# Possible solution:
# Using `file.close()`:
expressions_file = open('expresiones.txt')
results_file = open('calculos.txt', 'w')
for line in expressions_file:
    operator, left_operand, right_operand = line.split(' ')
    left_operand = int(left_operand)
    right_operand = int(right_operand)
    if operator == '+':
        result = left_operand + right_operand
    elif operator == '-':
        result = left_operand - right_operand
    elif operator == '*':
        result = left_operand * right_operand
    elif operator == '/':
        result = left_operand / right_operand
    elif operator == '%':
        result = left_operand % right_operand
    else:
        raise ValueError(f"Operator {operator} is not defined.")
    results_file.write(f"{left_operand} {operator} {right_operand} = {result}\n")
expressions_file.close()
results_file.close()

# Using `with` keyword.
# Note how we can open two files on the same line instead of writing:
# with open('expresiones.txt') as expressions_file:
#     with open('calculos.txt', 'w') as results_file:
#         ...  # rest of the code goes here
with open('expresiones.txt') as expressions_file, open('calculos.txt', 'w') as results_file:
    for line in expressions_file:
        operator, left_operand, right_operand = line.split(' ')
        left_operand = int(left_operand)
        right_operand = int(right_operand)
        if operator == '+':
            result = left_operand + right_operand
        elif operator == '-':
            result = left_operand - right_operand
        elif operator == '*':
            result = left_operand * right_operand
        elif operator == '/':
            result = left_operand / right_operand
        elif operator == '%':
            result = left_operand % right_operand
        else:
            raise ValueError(f"Operator {operator} is not defined.")
        results_file.write(f"{left_operand} {operator} {right_operand} = {result}\n")
        
# -------------------------------------------------------------------------------------------------
# Advanced solution.
# We can avoid repetition by using a dictionary: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
# This dict will map operator symbols to corresponding functions.
# In order to use math operators as functions, we will use `operator` library:
# https://docs.python.org/3/library/operator.html
# See also: https://stackoverflow.com/a/40452276/7851470
import operator

functions_per_symbol = {'+': operator.add,
                        '-': operator.sub,
                        '*': operator.mul,
                        '/': operator.truediv,
                        '%': operator.mod}
with open('expresiones.txt') as expressions_file, open('calculos.txt', 'w') as results_file:
    for line in expressions_file:
        operator, left_operand, right_operand = line.split(' ')
        left_operand = int(left_operand)
        right_operand = int(right_operand)
        try:
            result = functions_per_symbol[operator](left_operand, right_operand)
        except KeyError:
            raise ValueError(f"Operator {operator} is not defined.")
        results_file.write(f"{left_operand} {operator} {right_operand} = {result}\n")
