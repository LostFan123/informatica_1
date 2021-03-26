# Task:
#   Define a vector of characters F that contains a sentence finished with character '.' such as
#   F=list(“Esto es una frase de prueba.”) and write a program that shows the first word of F that starts
#   with a lower case vocal. In the example it will show “es”.
#   Note1: words are separated by space characters ' '.
#   Note2: lower case vocal letters are 'a', 'e', 'i', 'o' and 'u'. Do not consider accents!

# -------------------------------------------------------------------------------------------------------
# Solution:
characters = list("Esto es una frase de prueba.")
is_word_found = False
index = 0
while not is_word_found and character != '.':
    is_first_letter = index == 0 or characters[index - 1] == ' '
    if is_first_letter:
        if character == 'a' or character == 'e' or character == 'i' or character == 'o' or character == 'u':
            is_word_found = True
    index += 1
    character = characters[index]
if is_word_found:
    while character != ' ' and character != '.':
        print(character)
        index += 1
        character = characters[index]
else:
     print("There is bo word starting with vocal")
        
# -------------------------------------------------------------------------------------------------------
# Advanced solution.
# Using `string.split` method to split a string into a list of words;
# using `next` with the given default value `None`
# to find the first word that starts with lowercase vowel 
# by checking the first characters against a set of vowels
characters = list("Esto es una frase de prueba.")
lowercased_vowels = {'a', 'e', 'i', 'o', 'u'}
string = ''.join(string)
words = string.split(' ')
first_vowel_word = next(word for word in words if word[0] in lowercased_vowels, None)
if first_vowel_word is not None:
    print(first_vowel_word)
else:
    print("There is bo word starting with vocal")
