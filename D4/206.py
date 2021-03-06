number = int(input("Number: "))
divisor = 2
divisors_sum = 0
while divisor <= number // 2:
    if number % divisor == 0:
        print("Divisor:", divisor)
        divisors_sum += divisor
    divisor += 1
print("Sum of the divisors:", divisors_sum)
