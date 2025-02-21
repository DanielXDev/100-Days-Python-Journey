from idlelib.sidebar import temp_enable_text_widget

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
result = []


# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

def encrypt(original_text, shift_amount):
    for letter in original_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift_amount) % 26
            result.append(alphabet[new_position])
        else:
            result.append(letter)
    encoded_text = ''.join(result)
    print(f"Here is the encoded result: {encoded_text}")
# encrypt(text, shift)
def decrypt(original_text, shift_amount):
    for letter in original_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position - shift_amount) % 26
            result.append(alphabet[new_position])
        else:
            result.append(letter)
    encoded_text = ''.join(result)
    print(f"Here is the decoded result: {encoded_text}")
# encrypt(text, shift)

def caesar(direct):
    if direct.lower() == "encode":
        encrypt(text, shift)
    elif direct.lower() == "decode":
        decrypt(text, shift)
    else:
        print("Wrong input!!!")

caesar(direction)


# encrypt(original_text=text, shift_amount=shift)



