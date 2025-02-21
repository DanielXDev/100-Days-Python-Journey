from art import logo

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

on_machine = True
profit = 0

print(logo)

def off_machine():
    global on_machine
    on_machine = False

def print_report(items):
    for item, amount in items.items():
        print(f"{item}: {amount}")
    print(f"profit: ${profit}")

def check_resources_sufficiency(choice, menu, machine_resources):
    enough_resources = True
    for ing, amount in menu[choice]["ingredients"].items():
        if amount > machine_resources[ing]:
            enough_resources = False
            print(f"Sorry there is not enough {ing}")
    if enough_resources:
        process_coin(choice)
    else:
        ask_user()


def process_coin(choice):
    penny = int(input("Penny:   "))
    nickel = int(input("Nickel:   "))
    dime = int(input("Dime:   "))
    quarter = int(input("Quarter:   "))
    user_coins = (0.01 * penny) + (0.05 * nickel) + (0.10 * dime) + (0.25 * quarter)
    transaction_successful(user_coins, choice)

def transaction_successful(money, choice):
    global profit
    if money < MENU[choice]["cost"]:
        print("Sorry that's not enough money. Money Refunded")
    else:
        profit += MENU[choice]["cost"]
        change = round(money - MENU[choice]["cost"], 2)
        if change != 0:
            print(f"Here is your ${change} change")
        make_coffee(choice)

def make_coffee(choice):
    for ing, amount in MENU[choice]["ingredients"].items():
        resources[ing] -= amount
    print(f"Here is your {choice}☕. Enjoy!!")





def ask_user():
    user_choice = input("What would you like? Espresso/Latte/Cappuccino  ").lower()
    if user_choice == "off":
        off_machine()
    elif user_choice == "report":
        print_report(resources)
    elif user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        check_resources_sufficiency(choice = user_choice, menu = MENU, machine_resources = resources)
while on_machine:
    ask_user()