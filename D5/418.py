# Task:
#   Write the code that determines if a vector containing character (a word) is palindrome, this is,
#   has the same content when reading from left to right than from right to left.

# ------------------------------------------------------------------------------------------------
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
    
# ------------------------------------------------------------------------------------------------
# Advanced solutions:
# Using a for-else loop construct with `break` statement
text = input("Enter text: ")
for index in range(len(text) // 2 + 1):
    if text[left_index] != text[len(text) - left_index - 1]:
        print("Not a palindrome")
        break
else:
    print("Palindrome")
    
# Using string slicing:
text = input("Enter text: ")
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
    
# ------------------------------------------------------------------------------------------------
# Common mistake:
# 1. Constructing new string containing the reversed string is not optimal memory-wise.
#    Probably, also won't be accepted on the exam as a "dyamically growing array".
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
