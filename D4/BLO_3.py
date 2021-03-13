# Task:
#   The gym opens a promotion to provide discounts to the spinning users that burn more
#   that 200 Kcal or to those users that burn more than 350 Kcal. Given a number with the digits-code
#   shown bellow, write the program that using the search schema informs if the user has won a discount. 
#   (Less significant digits -the ones on the right- are for the initial exercises)
#   code exercise desc Kcal
#   1 running 5' 50
#   2 elliptical 5' 20
#   3 lift weight 5’ 15
#   4 abdominals 35
#   5 spinning 1h 180
#   EXAMPLE: The code 334351 obtains the discount after considering digits 1 and 5 

# ------------------------------------------------------------------------------------------------
# Possible solution:
code = int(input('Input your number: '))
calories = 0
discount = False
spinning_discount = False
while code != 0 and not discount:
    code, digit = divmod(code, 10)
    if digit == 1:
        calories += 50
    if digit == 2:
        calories += 20
    if digit == 3:
        calories += 15
    if digit == 4:
        calories += 35
    if digit == 5:
        calories += 180
        spinning_discount = True
    if spinning_discount and calories >= 200:
        discount = True
    elif calories >= 350:
        discount = True
if discount:
    print('User has won a discount.')
else:
    print('User has not won a discount.')

# ------------------------------------------------------------------------------------------------
# Advanced solutions:
#   Using a for-else loop construct with `break` statement:
code = int(input('Input your number: '))
calories = 0
spinning_discount = False
for digit in code:
    if digit == 1:
        calories += 50
    if digit == 2:
        calories += 20
    if digit == 3:
        calories += 15
    if digit == 4:
        calories += 35
    if digit == 5:
        calories += 180
        spinning_discount = True
    if spinning_discount and calories >= 200 or calories >= 350:
        print('User has won a discount.')
else:
    print('User has not won a discount.')

    
# ------------------------------------------------------------------------------------------------
# Advanced solution:
#   Using a dictionary.
kcal_per_digit = {'1': 50, '2': 20, '3': 15, '4': 35, '5': 180}
code = input("Code: ")
calories = 0
spinning_discount = False
for digit in code:
    if digit == 5:
        spinning_discount = True
    calories += kcal_per_digit[digit]
if spinning_discount and calories >= 200 or calories >= 350:
    print('User has won a discount.')
else:
    print('User has not won a discount.')
    
# Or alternatively using a `sum` function and checking for a presence of character '5' in the code:
kcal_per_digit = {'1': 50, '2': 20, '3': 15, '4': 35, '5': 180}
code = input("Code: ")
calories = sum(kcal_per_digit[digit] for digit in code)
if calories >= 350 or calories >= 200 and '5' in code:  # Note the order: `'5' in code` won't be checked if `calories < 200`
    print('User has won a discount.')
else:
    print('User has not won a discount.')
