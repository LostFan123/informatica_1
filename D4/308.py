# 1. Incorrectly understood task. We need a sequence of numbers, not digits:
sequence=int(input("Number: "))
count_of_even_digits=0
while sequence!=0:
  digit_=sequence%10
  sequence=sequence//10
  print(digit_)
  if digit_%2==0:
   count_of_even_digits+=1
  elif digit_==0:
   count_of_even_digits+=1
print("This is the number of even digits introduced: ",count_of_even_digits)

# Possible solution:
are_all_even = True
while True:
    number = int(input("N: "))
    if number == 0:
        break
    if number % 2 != 0:
        are_all_even = False
if are_all_even:
    print("All numbers are even")
else:
    print("Not all numbers are even")
