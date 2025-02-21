print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?"))
    if age < 12:
        print("You're going to pay $5.")
    elif age <= 18:
        print("You're going to pay $7.")
    else:
        print("You're are going to pay $12.")
else:
    print("Sorry you have to grow taller before you can ride.")
