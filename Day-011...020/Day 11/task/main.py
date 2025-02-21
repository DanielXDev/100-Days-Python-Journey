import random
import art

play_game = False
def ask_user():
    global play_game
    want_to_play = input("Do you want to play a game of jack? y/n \n").lower()
    if want_to_play == "y":
        print("\n" * 15)
        play_game = True
    return play_game
ask_user()
# print(ask_user())
while play_game:
    print(art.logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_cards = []
    computer_cards = []
    user_cards.extend(random.sample(cards, 2))
    computer_cards.extend(random.sample(cards, 2))
    continue_game = True
    while continue_game:
        print(f"Your cards: {user_cards}     sum: {sum(user_cards)} ")
        print(f"Computer first hand: {computer_cards[0]}")
        computer_blackjack = False
        user_blackjack = False
        draw_new = input("Do you want to draw a new card? y/n \n")
        if draw_new == "n":
            continue_game = False
            while sum(computer_cards) < 17:
                computer_cards.append(random.choice(cards))
            print(f"Your final hand: {user_cards}   total: {sum(user_cards)}")
            print(f"Computer's final hand: {computer_cards}     total: {sum(computer_cards)}")
            if sum(user_cards) == 21 and len(user_cards) == 2:
                # print(f"User has 11")
                user_blackjack = True
                user_cards = [0]
            if sum(computer_cards) == 21 and len(computer_cards) == 2:
                # print("Computer has 11")
                computer_blackjack = True
                computer_cards = [0]
            if user_blackjack and not computer_blackjack:
                print("You win. Blackjack!!")
            elif computer_blackjack:
                print("Computer wins with Blackjack. You loose!!")
            elif sum(computer_cards) > 21:
                print("Computer final hand is more than 21. You win!!")
            elif sum(user_cards) > sum(computer_cards):
                print("You win!!")
            elif sum(user_cards) == sum(computer_cards):
                print("Draw")
            elif sum(computer_cards) > sum(user_cards):
                print("Computer wins!!")

            play_game = False
            # print("\n" * 15)
            ask_user()
        elif draw_new == "y":
            for hand in user_cards:
                if hand == 11:
                    index_of = user_cards.index(hand)
                    user_cards[index_of] = 1
            user_cards.append(random.choice(cards))
            if sum(user_cards) > 21:
                print(f"Your final hand: {user_cards}   total: {sum(user_cards)}")
                print(f"Computer's final hand: {computer_cards}     total: {sum(computer_cards)}")
                print("Your final hand is over 21. Computer Wins!!")
                continue_game = False
                ask_user()
            else:
                continue_game = True

