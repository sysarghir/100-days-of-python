### Rock Paper Scissors Game
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player_1 = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: \n"))
computer = random.randint(0,2)
rps = [rock, paper, scissors]


if player_1 >= 3 or player_1 < 0:
    print("You typed an invalid number, you LOSE ! ")
elif player_1 == 0 and computer == 2:
    print(rps[player_1])
    print("\n Computer chose: ")
    print(rps[computer])
    print("You WON! ")
elif player_1 == 1 and computer == 0:
    print(rps[player_1])
    print("\n Computer chose: ")
    print(rps[computer])
    print("You WON! ")
elif player_1 == 2 and computer == 1:
    print(rps[player_1])
    print("\n Computer chose: ")
    print(rps[computer])
    print("You WON! ")
elif player_1 == computer:
    print(rps[player_1])
    print("\n Computer chose: ")
    print(rps[computer])
    print("Its a DRAW ")
else:
    print(rps[player_1])
    print("\n Computer chose: ")
    print(rps[computer])
    print("You LOSE! ")






