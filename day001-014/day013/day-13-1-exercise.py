# ## Debug Odd or Even
# # Instructions
# - Read this the code in main.py 
# - Spot the problems 🐞. 
# - Modify the code to fix the program. 
# Fix the code so that it works and passes the tests when you submit. 
# # Hint
# 1. Review the previous lesson and go through the 10 steps to tackle these debugging problems.
# # Solution
# [https://repl.it/@appbrewery/day-13-1-solution](https://repl.it/@appbrewery/day-13-1-solution)



number = int(input("Which number do you want to check?"))

if number % 2 == 0:   # should be == ( is equal )  instead of = ( give it the value )
  print("This is an even number.")
else:
  print("This is an odd number.")
  
