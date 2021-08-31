import sys
import os

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

order = "yada"
quarters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01


def update_bag(coffee):
    for key in MENU[coffee]["ingredients"]:
        resources[key] = resources[key] - MENU[coffee]["ingredients"][key]
    if "Money" in resources:
        resources["Money"] = resources["Money"] + MENU[coffee]["cost"]
    else:
        resources["Money"] = MENU[coffee]["cost"]


def print_resources(bag):
    for k in bag:
        print(f"{k.capitalize()}: {bag[k]} ")


def check_bag(coffee):
    for key in MENU[coffee]["ingredients"]:
        if MENU[coffee]["ingredients"][key] > resources[key]:
            return key
        else:
            return "brew"


def brew_coffee(coffee):
    have_ingredients = check_bag(coffee)
    if have_ingredients == "brew":
        print("please insert coins")
        insert_quarters = int(input("How many quarters?: "))
        insert_dimes = int(input("How many dimes?: "))
        insert_nickles = int(input("How many nickles?: "))
        insert_pennies = int(input("How many pennies?: "))
        coins_inserted = insert_quarters * quarters + insert_dimes * dimes + insert_nickles * nickles + insert_pennies * \
                         pennies
        return_change = round(coins_inserted - MENU[coffee]["cost"], 2)
        print(f"Here is ${return_change} in change.")
        print(f"Here is your {coffee} ☕. Enjoy!")
        update_bag(coffee)
    else:
        print(f"Sorry there is not enough {have_ingredients}")


while order != "off":

    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order == "report":
        print_resources(resources)
    elif order == "off":
        os.system("cls")
        sys.exit("It is now SAFE to turn off your computer")
    elif order.lower() != "espresso" or order.lower() != "latte" or order.lower() != "cappuccino":
        print(f"Your {order} costs: ${MENU[order]['cost']}")
        brew_coffee(order)
    else:
        print("We cannot brew your choice of delicacy.")
        print("Please try again ")
