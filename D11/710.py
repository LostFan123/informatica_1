# Task:
#   (A) Write a function contar_ceros that receives a vector and returns the number of values equal to
#   zero. Test it writing a small main program
#   (B) Create a similar function contar for the following main program
#   frase = input ('Enter a sentence');
#   letra = input ('Enter a letter');
#   n = contar(frase, letra);
#   print(“Letter “+letra+” appears “+str(n)+ “ times in sentence ”+frase)
#   (C) Write a new function top_letter to calculate and return the most frequent letter in a sentence that
#   enters as input argument. Use the function contar to do such functionality.
#   (D) Finally, write the main program to test the above function with a sentence given by the user
#   from the keyboard.

# --------------------------------------------------------------------------------------------------------
# Possible solution:
# A:
#   if we are not allowed to use `count` method:
def contar_ceros(values):
    zeros_count = 0
    for value in values:
        if value == 0:
            zeros_count += 1
    return zeros_count

#   if we don't have any artificial restrictions:
def contar_ceros(values):
    return values.count(0)

# B:
# Note: we should lowercase the input strings because we want, for example, "A" to be equal to "a".
#   if we are not allowed to use `count` method:
def contar(string, letter):
    letter = letter.lower()
    letter_count = 0
    for char in string.lower():
        if char == letter:
            letter_count += 1
    return letter_count

#   if we don't have any artificial restrictions:
def contar(string, letter):
    string = string.lower()
    return string.count(letter.lower())
                        
#   Usage example:
frase = input('Enter a sentence')
letra = input('Enter a letter')
n = contar(frase, letra)
print(f"Letter {letra} appears {n} times in sentence {frase}")         

# C:
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
def top_letter(string):
    most_frequent_letter_count = 0
    for letter in ALPHABET:
        count = contar(string, letter)
        if count > most_frequent_letter_count:
            most_frequent_letter_count = count
            most_frequent_letter = letter
    if most_frequent_letter_count == 0:
        raise ValueError("Input sentence doesn't contain any letters.")
    return most_frequent_letter

# D:
sentence = input("Enter a sentence: ")
print(top_letter(sentence))


# --------------------------------------------------------------------------------------------------------
# Advanced solution.
#   Using type hints.
#   Using `string.ascii_lowercase` to get an alphabet.
#   Using `max` built-in function with generator expression:
#   Note that the task explicitly asks us to use `contar` function. 
#   If not for this restriction, we could've used `collections.Counter` instead:
#   https://docs.python.org/3/library/collections.html#collections.Counter
# A:
from typing import List  # this is not necessary in Python >= 3.9, you can just use `list` instead

def contar_ceros(values: List[float]) -> int:
    return values.count(0)

# B:
def contar(string: str, letter: str) -> int:
    string = string.lower()
    return string.count(letter.lower())

# C:
from string import ascii_lowercase

def top_letter(string):
    count, letter =  max((contar(string, letter), letter) 
                         for letter in ascii_lowercase)
    if count == 0:
        raise ValueError("Input sentence doesn't contain any letters.")
    return letter

# D would be the same
