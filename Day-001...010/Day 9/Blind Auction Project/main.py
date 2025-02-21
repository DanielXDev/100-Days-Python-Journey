import art
# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
print(art.logo)
auction = {}
auctioning = True
while auctioning:
    user_name = input("What is your name?")
    user_bid = int(input("What is your bid amount? $"))
    auction[user_name] = user_bid

    new_bid = input("Is there another bid? Yes/No").lower()
    if new_bid == "no":
        highest_bid = 0
        bidder = ""
        for key in auction:
            # print(auction[key])
            if auction[key] > highest_bid:
                highest_bid = auction[key]
                bidder = key
        print("\n" * 25)
        print(f"The highest bidder is {bidder} with ${highest_bid} bid.")
        auctioning = False
    else:
        print("\n" * 25)

