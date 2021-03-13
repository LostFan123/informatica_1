# Task:
#   Count the space characters (' ') of a sentence contained in vector S. For instance, S=”This
#   exercises should give a result of 9 white spaces”


# ------------------------------------------------------------------------------------------------
# Possible solution using a while loop:
text = str(input("Write a sentence: "))
index = 0
spaces_count = 0
while index < len(text):
    if text[index] == ' ':
        spaces_count += 1
print(spaces_count)

# Possible solution using for-loop:
text = str(input("Write a sentence: "))
spaces_count = 0
for character in text:
    if character == ' ':
        spaces_count += 1
print(spaces_count)

# ------------------------------------------------------------------------------------------------
# Advanced solution.
# Strings have a special `count` method for this task. This won't be accepted on the exams, though!
text = str(input("Write a sentence: "))
print(text.count(' '))
