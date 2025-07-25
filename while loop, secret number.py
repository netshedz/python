'''The program first prints a multi-line welcome message.

It prompts the user to guess the number.

If the guess is incorrect, it loops with a taunting message.

When the guess is correct, it congratulates the user and ends the loop.'''

secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

# Start the game loop
guess = int(input("Enter your guess: "))

while guess != secret_number:
    print("Ha ha! You're stuck in my loop!")
    guess = int(input("Try again: "))

# When the correct number is guessed
print(f"{secret_number}")
print("Well done, muggle! You are free now.")
