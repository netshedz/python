'''ask the user to enter a word;
use user_word = user_word.upper() to convert the word entered by the user to upper case; we'll talk about string methods and the upper() method very soon - don't worry;
use conditional execution and the continue statement to "eat" the following vowels A, E, I, O, U from the inputted word;
assign the uneaten letters to the word_without_vowels variable and print the variable to the screen.'''

user_word = input("Enter a word: ")
user_word = user_word.upper()
no_vowels = ""  # Start with an empty string
vowels = ["A","E","I","O","U"]

for letter in user_word:
    if letter.upper() in vowels:
        continue  # Skip vowels
    no_vowels += letter  # Add non-vowel to the new string

print("Word without vowels:", no_vowels)
