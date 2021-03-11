# 1. Constructing new string containing the reversed string is not optimal:
text = input("Enter text: ")
index = len(text) - 1
reversed_text = ""
while index >= 0:
    reversed_text += text[index]
    index -= 1
if reversed_text == text:
    print("Palindrome")
else:
    print("Not a palindrome")
   
# Possible solution:
text = input("Enter text: ")
left_index = 0
is_palindrome = True
while left_index < len(text) // 2 and is_palindrome:
    right_index = len(text) - left_index - 1
    if text[left_index] != text[right_index]:
        is_palindrome = False
if is_palindrome:
    print("Palindrome")
else:
    print("Not a palindrome")
    
# How it is actually done. Probably, won't be accepted on the exams, though:
text = input("Enter text: ")
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
    
