# print("Welcome to your AI Mathematical reminder checker.")
# first_number = int(input("Numerator?"))
# second_number = int(input('Denominator?'))
# answer = int(first_number / second_number)
# reminder = first_number % second_number
# if reminder == 0:
#     print(f"The answer is {answer} and there is no reminder from the fraction")
# else:
#     print(f"The answer is {answer} with {reminder} reminder")

number = int(input("Type in a number."))
check_odd_even = number % 2
if check_odd_even == 0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")
