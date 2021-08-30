# Higher Lower Game

from art import logo
from art import vs
from game_data import data
import os as os
import random


persona_1 = random.choice(data)
persona_2 = random.choice(data)
follower_count_a = persona_1["follower_count"]
follower_count_b = persona_2["follower_count"]

game_over = False
score = 0


while not game_over:
    os.system("cls")
    print(logo)
    if score > 0:
        print (f"You are right! Current score: {score} ")
    print(f"Compare A: {persona_1['name']}, a {persona_1['description']}, from {persona_1['country']} \n")
    print(vs)
    print("")
    print(f"Compare B: {persona_2['name']}, a {persona_2['description']}, from {persona_2['country']} \n")
    answer = input("Who has more followers? Type 'A' or 'B': ")

    if answer.upper() == "A":
        if follower_count_a > follower_count_b:
            persona_1 = persona_2
            score += 1
        else:
            os.system("cls")
            print(logo)
            print(f"Sorry thats wrong. Final Score: {score} ")
            game_over = True

    elif answer.upper() == "B":
        if follower_count_b > follower_count_a:
            persona_1 = persona_2
            score += 1
        else:
            os.system("cls")
            print(logo)
            print(f"Sorry thats wrong. Final Score: {score} ")
            game_over = True
    persona_2 = random.choice(data)
    follower_count_b = persona_2["follower_count"]




