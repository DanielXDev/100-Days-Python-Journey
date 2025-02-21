print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
tip_amount = bill * tip / 100
first_total_bill = bill + tip_amount
people = int(input("How many people to split the bill? "))
last_bill = round(first_total_bill / people, 2)
print(f"Each person should pay: {last_bill}")


