# Caesar Cipher 

from typing import Annotated
import art as art

display = []

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
continue_maybe = True

def caesar(input_text,shift_no,direction_info):
    final_text = ""
    for letter in input_text:
        if not letter in alphabet:
            final_text += letter
        elif direction_info == "decode":
            if alphabet.index(letter) - shift_no < 0:
                final_text += alphabet[alphabet.index(letter) - shift_no + 26]
            else:
                final_text += alphabet[alphabet.index(letter) - shift_no]
        elif direction_info == "encode":
            if alphabet.index(letter) + shift_no  > 25:
                final_text += alphabet[alphabet.index(letter) + shift_no - 26]
            else:
                final_text += alphabet[alphabet.index(letter) + shift_no]
    print(F"Your {direction} text is: {final_text}")



# if shift >= 26:
#     shift = shift % 26


#caesar(text,shift,direction)

while continue_maybe:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if shift >= 26:
        shift = shift % 26

    caesar(text,shift,direction)

    maybe = input("Type 'yes' if you want to go again. Otherwise type 'no':\n").lower()
    if maybe == "no":
        continue_maybe = False
    elif maybe != "no" and maybe != "yes":
        print("INVALID INPUT \n WE QUIT NOW !!!! \n")
        continue_maybe = False




