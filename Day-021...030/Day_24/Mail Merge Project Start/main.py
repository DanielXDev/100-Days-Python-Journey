#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

# import the name list
with open("./Input/Names/invited_names.txt", mode="r") as name_list:
    names = name_list.readlines()

def open_letter():
    with open("./Input/Letters/starting_letter.txt", mode="r") as letter:
        return letter.read()

# for each name in the guest_list, replace name
for name in names:
    starting_letter = open_letter()
    with open(f"./Output/ReadyToSend/{name.strip()}.docx", mode="w") as new_letter:
        replaced_letter = starting_letter.replace("[name]", f"{name.strip()}")
        new_letter.write(f"{replaced_letter}")





