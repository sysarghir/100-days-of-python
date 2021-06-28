# Final Project: Escaping the Maze
# Reeborg`s World:
#
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
#
#
# ToDo: debug the weird behaviour:

### Commenting the code so the VScode doesnt complain ###
'''

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def go_captain_go():
    while wall_on_right() and front_is_clear():
        move()
    if wall_in_front() and wall_on_right():
        turn_left()
    elif right_is_clear():
        turn_right()
        move()
        
while not at_goal():
    go_captain_go()


'''