############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


from art import logo
import os as os
import random



cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]



# play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n")

# if play_game == "y":
#     keep_playing = True
# elif play_game == "n":
#     keep_playing = False
# else:
#     print("Invalid Input.... Exiting now.....")


def play_game():
    play_me = input("Do you want to play a game of Blackjack? Type 'y' or 'n' ")
    if play_me == "y":
        return True
    elif play_me == "n":
        return False
    else:
        print("Invalid Input.... Exiting now.....")
        return False


def draw_cards(player,number_to_draw):
    for i in range(0,number_to_draw):
        player.append(random.choice(cards)) 

def score(player):
    cards_score = 0
    for i in range (0, len(player)):
        cards_score += player[i]
    if cards_score > 21 and 11 in player:
        index = player.index(11)
        player[index] = 1
        cards_score = cards_score - 10
    return cards_score

def game_over():
    player_score = score(player_cards)
    cp_score = score(cp_cards)
    print(f"Your final hand: {player_cards}, final score: {player_score}")
    while cp_score < 17:
        draw_cards(cp_cards,1)
        cp_score = score(cp_cards)
    print(f"Computer final hand: {cp_cards}, final score: {cp_score}")
    if cp_score > 21 and player_score < 22:
        print("Opponent went over. YOU WIN !!!")
    elif player_score > 21 and cp_score < 22:
        print("You went over. You Lose ")
    elif cp_score > player_score:
        print("Computer win")
    elif cp_score < player_score:
        print("You win")
    else:
        print("Its a draw !")


keep_playing = play_game()

while keep_playing:
    os.system("cls")
    print(logo)
    player_cards = []
    cp_cards = []
    
    draw_cards(player_cards,2)
    draw_cards(cp_cards,2)

    player_score = score(player_cards)
    cp_score = score(cp_cards)

    print(f"Your cards: {player_cards}, current score: {player_score}")
    print(f"Computer first card: {cp_cards[0]}")

    more_cards = input("Type 'y' to get another card, type 'n' to pass: ")

    while more_cards == "y":
        draw_cards(player_cards,1)
        player_score = score(player_cards)
        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Computer first card: {cp_cards[0]}")
        if player_score > 21:
            break
        more_cards = input("Type 'y' to get another card, type 'n' to pass: ")
        
    game_over()
    keep_playing = play_game()








