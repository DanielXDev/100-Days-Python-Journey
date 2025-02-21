import art
import random

#Creating global and normal variables
easy = 10
hard = 5
attempt = 0
game_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
guessed_number = random.choice(game_number)

# Print the game to the user
print(art.logo)
print("Welcome to Guess It.")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard':  ").lower()

# creating attempts based on the level of difficulty the user choose.
if difficulty == "easy":
    attempt = easy
elif difficulty == "hard":
    attempt = hard
else:
    print("Wrong Input")

#Taking user guess and showing how guess they have left and if they got it right.
while attempt != 0:
    print(f"You have {attempt} guess left.")
    user_guess = int(input("Make a guess:   "))
    if user_guess == guessed_number:
        print("Yes you got it right. You win!!")
        attempt = 0
    else:
        attempt -= 1
        if user_guess > guessed_number:
            print("Too high")
        elif user_guess < guessed_number:
            print("Too low")
        if attempt == 0:
            print("You've ran out of guess.")