# Hangman game created for 100d of code

import random
import hangman_art as art
import hangman_words as w


display = []

print(art.logo)
stages = art.stages

chosen_word = random.choice(w.word_list)

#Testing word code
#print(f'Pssst, the solution is {chosen_word}.')



for i in range(0,len(chosen_word)):                                                         # createa a new list with all letters hidden = _ 
    display.append("_")

lives = 6

while "_" in display:
    guess = input("\n\nGuess a letter: ").lower()
    if not guess in chosen_word:    
        if lives == 0:                                                                    # GAME OVER if not guessing the word
            print(stages[lives])
            print("You Lose !")
            break
        else:
            print(f"You guessed {guess}, that's not in the word. You lose a life. \n")     # If you didnt guess a correct letter will 
            print(stages[lives])                                                           # substract a life and print the current hangman 
            lives -= 1
    if guess in display:
        print(f"You`ve already guessed {guess}. \n")                                       # points out the letter is already part of the word
        
    for i in range(0,len(chosen_word)):                                                    # if the letter is part of the word it will be added to a list 
        if chosen_word[i] == guess:                                                        # and be visible on the display
            display[i] = guess

    for i in range(len(display)):                                                          # print out the current discovered letters
        print(f"{display[i]}", end = " ")

    if not "_" in display:                                                                 # when you found the word will display the "WIN" message 
        print("\nYou win !")
           

