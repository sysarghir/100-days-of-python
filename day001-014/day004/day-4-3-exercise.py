# #Treasure Map
# ![](https://cdn.fs.teachablecdn.com/wiFJAkZZSG2RpGsxYgDO)
# Instructions
# You are going to write a program which will mark a spot with an X.
# In the starting code, you will find a variable called ```map```.
# This ```map``` contains a nested list.
# When ```map``` is printed this is what the nested list looks like:
# ```
# ['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']
# ```
# In the starting code, we have used new lines (```\n```) to format the three rows into a square, like this:
# ```
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# ```
# This is to try and simulate the coordinates on a real map. 
# ![](https://res.cloudinary.com/dk-find-out/image/upload/q_80,w_1440,f_auto/Co-ordinates_oggjzg.jpg)
# Your job is to write a program that allows you to mark a square on the map using a two-digit system. The first digit is the vertical column number and the second digit is the horizontal row number. e.g.:
# ![](https://cdn.fs.teachablecdn.com/2vnboIYTFFruvl9FJ2w5)
# First your program must take the user input and convert it to a usable format. 
# Next, you need to use it to update your nested list with an "x". 
# Example Input 1
# column 2, row 3 would be entered as:
# ```
# 23
# ```
# Example Output 1
# ```
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', 'X', '⬜️']
# ```
# Example Input 2
# column 3, row 1 would be entered as:
# ```
# 31
# ```
# Example Output 2
# ```
# ['⬜️', '⬜️', 'X']
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# ```
# e.g. When you hit **run**, this is what should happen: 
# ![](https://cdn.fs.teachablecdn.com/5hliFjyIR96LdestyfPd)
# Hint
# 1. Remember that Lists start at index 0!
# 2. ```map``` is just a variable that contains a nested list. It's not related to the map function in Python.
# Solution
# [https://repl.it/@appbrewery/day-4-3-solution](https://repl.it/@appbrewery/day-4-3-solution)
#
#
# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(" [\' 1\', \' 2\', \' 3\']")
print(f"1{row1}\n2{row2}\n3{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# column = int(position[0])
# column -= 1
# actual_row = position[1]

# find_the_row = "row" + actual_row

# if find_the_row == "row1":
#     row1[column] = "X"
# elif find_the_row == "row2":
#     row2[column] = "X"
# elif find_the_row == "row3":
#     row3[column] = "X"
    
####### easier solution:

column = int(position[0])
actual_row = int(position[1])

map[actual_row-1][column-1] = " X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(" [\' 1\', \' 2\', \' 3\']")
print(f"1{row1}\n2{row2}\n3{row3}")