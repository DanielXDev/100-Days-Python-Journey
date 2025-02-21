import random
import hangman_words
import hangman_art

hidden_chosen = random.choice(hangman_words.word_list)
guessed_letter = []

print(hangman_art.logo)
print("Welcome to Hangman Game.")
print(hidden_chosen)
game_over = False
lives = 6
while not game_over:
    print(f"You have {lives}/6 left")
    user_guess = input("Guess a letter in the hidden word.").lower()
    # print(guessed_letter)
    dash = ""
    if user_guess not in hidden_chosen:
        lives -= 1
        print(f"Wrong!!!!!!")
    elif user_guess in guessed_letter:
        print("You already added that.")
    for letter in hidden_chosen:
        if letter == user_guess:
            dash += letter
            guessed_letter.append(user_guess)
        elif letter in guessed_letter:
            dash += letter
            # print(letter)
        else:
            dash += "_"
        dash = dash
    print(dash)
    if "_" not in dash:
        game_over = True
        print("You Win.")
    elif lives == 0:
        game_over = True
        print(f"You lose \n The word is {hidden_chosen}")