#Import random, art and list

import random

from art import logo
from art import vs
from game_data import data

#Define global constant & var
#Define first and second opt

continue_game = True
choices_list = []
user_score = 0

#Display logo

print(logo)

#pick two random dic in the list as the choices
def game():
    global user_score
    # index_of_ans = ""
    # index_of_other = ""
    choices_list.extend(random.sample(data, 2))
    # print(choices_list)
    #Display to the user and ask.
    print(f"Compare A: {choices_list[0]["name"]}, a {choices_list[0]["description"]} from {choices_list[0]["country"]}")
    print(vs)
    print(f"Against B: {choices_list[1]["name"]}, a {choices_list[1]["description"]} from {choices_list[1]["country"]}")
    user_answer = input("Who has more followers? Type 'A' or 'B':   ")
    if user_answer == "A":
        index_of_ans = 0
        index_of_other = 1
    else:
        index_of_ans = 1
        index_of_other = 0
    # print(index_of)
    #Determine if the user is correct or not

    if choices_list[index_of_ans]["follower_count"] > choices_list[index_of_other]["follower_count"]:
        # If yes add 1 to the user score and pick another random dict as the second choice while making the prev second choice as the first.
        choices_list[0] = choices_list[1]
        choices_list[1] = random.choice(data)
        user_score += 1
        print(logo)
        print(f"You are right, your score is: {user_score}")
        # Then continue game
        game()
    else:
        # If wrong, display user  score and end game.
        print("\n" * 15)
        print(logo)
        print(f"You got it wrong, your final score is {user_score}")


game()