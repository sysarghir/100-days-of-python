#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import os as os
import random

os.system("cls")
print(logo)

print("Welcome to the Number Guessing Game!")
print("I`m thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5
else:
    print("Input not recognised... EXITING NOW !!!!")

random_number = random.randrange(0,101)

#print(f"Pssssst, the correct answer is {random_number}")

def guess_the_number():
    global attempts
    global random_number

    print(f"You have {attempts} attempts remaining to guess the number.")
    make_guess = int(input("Make a guess: "))
    attempts = attempts - 1
    if make_guess > random_number:
        print("Too high")
    elif make_guess < random_number:
        print("Too Low")
    elif attempts == 0:
        print(f"Tou`re run out of guesses, you lose. The number was {random_number} !!")
    else:
        print(f"You got it! The answe was {random_number} !!")
        attempts = 0


while attempts != 0:
    guess_the_number()