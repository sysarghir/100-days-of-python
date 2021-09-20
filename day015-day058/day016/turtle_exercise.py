# OOP Exercises

from turtle import Turtle, Screen
from prettytable import PrettyTable


# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# #timmy.color("SpringGreen2")
# timmy.color("red", "black")
# timmy.forward(100)
# timmy.circle(50)
#
# my_screen = Screen()
# my_screen.canvheight = 640
# my_screen.canvwidth = 480
#
# print(my_screen.canvheight)
# print(my_screen.canvwidth)
# my_screen.exitonclick()


table = PrettyTable()


table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align["Pokemon Name"] = "l"
table.align["Type"] = "r"
print(table)