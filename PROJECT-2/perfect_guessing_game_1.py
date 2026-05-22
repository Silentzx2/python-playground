# Project nane is Perfect guessing game
# The game will generate a random number between 1 and 100 and the player has to
# guess the number. The game will give feedback on whether the guess is too low, too high, or correct.
# The player will have a limited number of attempts to guess the number correctly.


# MODEULS
import random

# VARIABLES
a = -1
guess = 1
RANDOM = random.randint(1, 10)


while (a != RANDOM):

       a = int(input("Guess the number: "))
       if (a >RANDOM):
            print("Too High! Try again.")
            guess += 1
       elif (a < RANDOM):
            print("Too Low! Try again.")
            guess += 1 

print(f"Congratulations! You guessed the {RANDOM} in {guess} attempts.")