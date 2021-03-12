# Task:
#   Write a program that reads from keyboard the value of a temperature in Fahrenheit and convert
#   it to Celsius. If you don’t remember the formula, look in the Internet how to do the conversion.
#   For instance, if we enter 80 then the program shall respond with 26.6 Celsius degrees.
#   Formula is: Celsius = ( Fahrenheit - 32 ) * 5/9

# ------------------------------------------------------------------------------------------------

# Solution:
fahrenheit = float(input("Temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5 / 9
print(celsius)

# ------------------------------------------------------------------------------------------------

# Advanced solution:
#   The solution above will print `26.666666666666668` for input 80.
#   If we actually need to truncate it and print it as `26.6 Celsius degrees`,
#   then we can use `math.trunc` function. 
#   Note that we cannot use `round(number, 1)` since it will round the result to 26.7
fahrenheit = float(input("Temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5 / 9
celsius = math.trunc(celsius * 10) / 10  # 26.(6) -> 266.(6) -> 266 -> 26.6
print(celsius, "Celsius degrees")
# or the last line rewritten using f-strings:
print(f"{celsius} Celsius degrees")
