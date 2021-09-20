from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

import sys
import os

make_me_a_coffee = CoffeeMaker()
produce = Menu()
rain_gold = MoneyMachine()
order = ""


while order != "off":

    order = input(f"What would you like? {produce.get_items()} ? \n")

    if order == "report":
        os.system(("cls"))
        make_me_a_coffee.report()
    elif order == "off":
        os.system("cls")
        sys.exit("It is now SAFE to turn off your computer")
    elif order == "profit":
        rain_gold.report()
    elif order.lower() == "espresso" or order.lower() == "latte" or order.lower() == "cappuccino":
        drink = produce.find_drink(order)
        print(f"Your {order} costs: {drink.cost}")
        have_ingredients = make_me_a_coffee.is_resource_sufficient(drink)
        if have_ingredients:
            # rain_gold.make_payment(drink.cost)
            if rain_gold.make_payment(drink.cost):
                make_me_a_coffee.make_coffee(drink)
    else:
        print("We cannot brew your choice of delicacy.")
        print("Please try again ")


