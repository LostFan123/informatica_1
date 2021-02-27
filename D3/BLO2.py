code = int(input("Code: "))
kcal_total = 0
while code != 0:
    digit = code % 10
    code = code // 10
    # The above two lines can be rewritten as:
    # code, digit = divmod(code, 10)
    if digit == 1:
        kcal = 50
    elif digit == 2:
        kcal = 20
    elif digit == 3:
        kcal = 15
    elif digit == 4:
        kcal = 35
    elif digit == 5:
        kcal = 180
    kcal_total += kcal
print(f"Total Kcal: {kcal_total}")
