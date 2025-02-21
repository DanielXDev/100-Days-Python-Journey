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
money = 0
coffee_machine = True
not_enough = False
print(logo)
while coffee_machine:
# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino)


    def start_order():
        return input("What would you like? (Espresso/Latte/Cappuccino)  ").lower()

    coffee = start_order()

# TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt
    if coffee == "off":
        # coffee_machine = False
        print(coffee_machine)
        break
    elif coffee == "report":
# TODO: 3. Print report.
        print(f"water: {resources["water"]}ml \nmilk: {resources["milk"]}ml \ncoffee: {resources["coffee"]}g \nmoney: ${money}")
        continue

# TODO 4. Check resources sufficient?
    if coffee == "espresso" or coffee == "latte" or coffee == "cappuccino":
        for ingredient, amount in MENU[coffee]["ingredients"].items():
            # print(ingredient)
            if amount > resources[ingredient]:
                print(f"Not enough {ingredient}.")
                not_enough = True
        if not_enough:
            break

# TODO 5. Process coins.
    penny = int(input("Penny:  "))
    nickel = int(input("Nickel:  "))
    dime = int(input("Dime:  "))
    quarter = int(input("Quarter:  "))
    user_money = (0.01 * penny) + (0.05 * nickel) + (0.10 * dime) + (0.25 * quarter)

# TODO 6. Check transaction successful?
    if user_money < MENU[coffee]["cost"]:
        print("Sorry that's not enough money, money refunded!!")
    else:
        user_change = round(user_money - MENU[coffee]["cost"], 2)
        money += MENU[coffee]["cost"]
        if user_change != 0:
            print(f"Here is your {user_change} change.")

# TODO 7. Make Coffee.
        for ing, am in MENU[coffee]["ingredients"].items():
            resources[ing] -= am
        print(f"Here is your {coffee}. Enjoy!☕")