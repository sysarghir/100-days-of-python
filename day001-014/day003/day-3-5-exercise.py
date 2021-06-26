#  Love Calculator
#  💪 This is a Difficult Challenge 💪
#  Instructions
# You are going to write a program that tests the compatibility between two people.  
# To work out the love score between two people:
# > Take both people's names and check for the number of times the letters in the word TRUE occurs. Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number. 
# For Love Scores **less than 10** or **greater than 90**, the message should be:
# `"Your score is **x**, you go together like coke and mentos."` 
# For Love Scores **between 40** and **50**, the message should be:
# `"Your score is **y**, you are alright together."`
# Otherwise, the message will just be their score. e.g.:
# `"Your score is **z**."`
# e.g. 
# `name1 = "Angela Yu"`
# `name2 = "Jack Bauer"`
# T occurs 0 times
# R occurs 1 time
# U occurs 2 times
# E occurs 2 times
# Total = 5
# L occurs 1 time
# O occurs 0 times
# V occurs 0 times
# E occurs 2 times
# Total = 3
# Love Score = 53
# Print: "Your score is 53."
#  Example Input 1
# ```
# name1 = "Kanye West"
# ```
# ```
# name2 = "Kim Kardashian"
# ```
#  Example Output 1
# ```
# Your score is 42, you are alright together.
# ```
#  Example Input 2
# ```
# name1 = "Brad Pitt"
# ```
# ```
# name2 = "Jennifer Aniston"
# ```
#  Example Output 2
# ```
# Your score is 73.
# ```
# e.g. When you hit **run**, this is what should happen:  
# ![](https://cdn.fs.teachablecdn.com/nfSILIPSNaIOwWhPR5vr)
# The testing code will check for print output that is formatted like one of the lines below:
# ```
# "Your score is 47, you are alright together."
# "Your score is 125, you go together like coke and mentos."
# "Your score is 54."
# ```
#  Hint
# 1. The `lower()` function changes all the letters in a string to lower case. 
# [https://stackoverflow.com/questions/6797984/how-do-i-lowercase-a-string-in-python](https://stackoverflow.com/questions/6797984/how-do-i-lowercase-a-string-in-python)
# 2. The `count()` function will give you the number of times a letter occurs in a string. 
# [https://stackoverflow.com/questions/1155617/count-the-number-occurrences-of-a-character-in-a-string](https://stackoverflow.com/questions/1155617/count-the-number-occurrences-of-a-character-in-a-string)
#  Test Your Code
# Before checking the solution, try copy-pasting your code into this repl: 
# [https://repl.it/@appbrewery/day-3-5-test-your-code](https://repl.it/@appbrewery/day-3-5-test-your-code)
# This repl includes my testing code that will check if your code meets this assignment's objectives. 
#  Solution
# [https://repl.it/@appbrewery/day-3-5-solution](https://repl.it/@appbrewery/day-3-5-solution)
#
#
#
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1 = name1.lower()
name2 = name2.lower()

t_occurs = name1.count("t")
r_occurs = name1.count("r")
u_occurs = name1.count("u")
e_occurs = name1.count("e")
l_occurs = name1.count("l")
o_occurs = name1.count("o")
v_occurs = name1.count("v")


t_occurs += name2.count("t")
print(f"T occurs {t_occurs} times")
r_occurs += name2.count("r")
print(f"R occurs {r_occurs} times")
u_occurs += name2.count("u")
print(f"U occurs {u_occurs} times")
e_occurs += name2.count("e")
print(f"E occurs {e_occurs} times")
first_total = int(t_occurs) + int(r_occurs) + int(u_occurs) + int(e_occurs)
print(f"Total = {first_total}")
l_occurs += name2.count("l")
print(f"L occurs {l_occurs} times")
o_occurs += name2.count("o")
print(f"O occurs {o_occurs} times")
v_occurs += name2.count("v")
print(f"V occurs {v_occurs} times")
print(f"E occurs {e_occurs} times")
second_total = int(l_occurs) + int(o_occurs) + int(v_occurs) + int(e_occurs)
print(f"Total = {second_total}")
love_score = str(first_total) + str(second_total)
love_score = int(love_score)

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.") 
elif 40 < love_score < 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")