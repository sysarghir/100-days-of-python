print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

choice_1 = input("You`re at a cross road. Where do you want to go? Type \"left\" or \"right\". \n")
choice_1 = choice_1.lower()
if choice_1 == "left":
    choice_2 = input("You come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. \nType \"swim\" to swim across. \n")
    choice_2 = choice_2.lower()
    if choice_2 == "wait":
        choice_3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. \nWhich color do you choose? \n")
        choice_3 = choice_3.lower()
        if choice_3 =="yellow":
            print("You enter a room with a lion. You are his lunch. GAME OVER!")
        elif choice_3 == "red":
            print("You get teleported to a far away planet where a klingon kill you. GAME OVER!")
        elif choice_3 == "blue":
            print("You found the tresure. you WIN!")
        else:
            print("we dont know how to type, do we ? GAME OVER! ")
    elif choice_2 == "swim":
        print("Lake is full of Piranha. you die. GAME OVER! ")
    else:
        print("we dont know how to type, do we ? GAME OVER! ")
elif choice_1 == "right":
    print("Rocks fall, you die. GAME OVER!")
else:
    print("we dont know how to type, do we ? GAME OVER! ")