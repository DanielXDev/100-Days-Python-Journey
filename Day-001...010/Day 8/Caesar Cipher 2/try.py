
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
result = []



def caesar(original_text, shift_amount):
    for letter in original_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if direction == "decode":
                new_position = (position - shift_amount) % 26
                result.append(alphabet[new_position])
            elif direction == "encode":
                new_position = (position + shift_amount) % 26
                result.append(alphabet[new_position])
            else:
                print("Wrong Input!!!")
        else:
            result.append(letter)
    encoded_text = ''.join(result)
    print(encoded_text)
caesar(text, shift)
