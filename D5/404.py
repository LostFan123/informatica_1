# 1. This is how it is actually done in real life, but, most probably, won't be accepted on the exams:
text = str(input("Write a sentence: "))
print(text.count(' '))

# Most probably, you will be asked to solve this task using loops.
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
