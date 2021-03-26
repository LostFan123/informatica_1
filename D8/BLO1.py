# Task:
#   Write a program that implements a CurrencyConverter (from euros to dollars and viceversa). The
#   program will read from the console a number and then a character. The number will hold the
#   quantity of money and the letter ('$' or 'E') will indicate the currency (Dollars or Euros)

# --------------------------------------------------------------------------------------------------
# Solution
money_amount = float(input("Enter quatity of money: "))
currency = input("Enter currency (E:Euros, $:Dollars)"
if currency == 'E':
    result = money_amount * 1.4
elif currency == '$':
    result = money_amount / 1.4
else:
    print(f"Currency {currency} is not available")
print(result, currency)
