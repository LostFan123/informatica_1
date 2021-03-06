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
