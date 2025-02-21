def calculate_love_score(m_name, f_name):
    letter_in_true = []
    letter_in_love = []
    name = (m_name + f_name).lower()
    print(name)
    for letters in "true":
       for l in name:
           if l == letters:
               letter_in_true.append(letters)
    for letter in "love":
       for l in name:
           if l == letter:
               letter_in_love.append(letters)
    print(letter_in_true)
    print(letter_in_love)
    print(str(len(letter_in_true)) + str(len(letter_in_love)))
male = input("What is his name?")
female = input("What is her name?")
calculate_love_score(male, female)