#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = ""
for n in range(0,nr_letters):
    password += str(random.choice(letters))

for n in range(0,nr_symbols):
    password += str(random.choice(symbols))

for n in range(0,nr_numbers):
    password += str(random.choice(numbers))

print(f"Simple password is: {password}")


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

#### or we can use the random.shuffle(list) to randomize a list.

weird_password = ""

char_limit = nr_letters + nr_symbols + nr_numbers
char_left = [nr_letters, nr_symbols, nr_numbers]
posible_chars = [letters, symbols, numbers]



while sum(char_left) > 0:
    ran_char = random.randint(0,2)
    if char_left[ran_char] > 0:
        weird_password += str(random.choice(posible_chars[ran_char]))
        char_left[ran_char] -= 1

print(f"A more complicated password would be: {weird_password}")