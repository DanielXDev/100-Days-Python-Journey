print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    bill = 0
    if age <= 12:
        bill = 5
        print("Kid tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")
    want_pictures = input("Do you want to snap pictures? y/n")
    if want_pictures == "y":
        bill += 3
        print(f"Your total bill is $    {bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
