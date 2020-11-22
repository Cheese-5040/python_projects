"""
Turtle Graphics - Game Programming
"""

import turtle
import random

import playsound

"""
    Variables
"""
# Part 1
# Set up variables

# Window size
window_height = 600
window_width = 600

# The screen update interval
update_time_interval = 25

# Parameters for controlling the width of the river
river_width = 400
min_river_width = 200

# Border parameters
border_height = 600

# Parameters for gradually decreasing river width
river_width_update = 0.5

# How far should we stay away from the borders
safe_distance_from_border = border_height / 2 + 3

# Parameters for enemies
total_number_of_enemies = 10
enemies = []
enemy_speeds = []
enemy_width = 100
enemy_height = 40
enemy_speed_min, enemy_speed_max = 1, 25

# How far should we stay away from the enemies
safe_distance_from_enemy = 15

"""
    Helper function and event handler functions
"""

# Part 6
# Show a message when the game ends
def gameover(msg):
    #print(msg)
    messegeTurtle = turtle.Turtle()
    messegeTurtle.color("red")
    messegeTurtle.up
    messegeTurtle.write(msg, align="center", font=("Arial", 24, "normal"))    
    playsound.play("gameover.wav")
# Part 2 (2 of 2)
# 2.2 Event handler function for the turtle.ondrag() event
def moveplayerturtle(x, y):
    playerTurtle.ondrag(None)
    # Allow the turtle to move within the window only
    if x > -window_width / 2 and x < window_width / 2:
        playerTurtle.goto(x, y)

    turtle.tracer(False) # Stop updating the screen (it will be updated in the next frame)

    #playerTurtle.ondrag(draw)
    playerTurtle.ondrag(moveplayerturtle)
# Event handler function for the turtle.ontimer() event
def updatescreen():
    """
        This function does:
            1. Decrease the width of the river
            2. Check if the player has hit the borders
            3. Move the enemies
            4. Check if the player has collided with an enemy
            5. Update the screen
            6. Schedule the next update
    """
    
    # Global variables that will be changed in the function
    global river_width

    # Part 4.2
    # Decrease the width of the river by river_width_update
    # until it reaches min_river_width
    if river_width > min_river_width:
        upper_river_border.sety(upper_river_border.ycor() - river_width_update)
        lower_river_border.sety(lower_river_border.ycor() + river_width_update)
        river_width -= river_width_update*2

    # Part 4.3
    # 4.3.1 Check if the player turtle has hit the borders
    # The vertical distance between the player turtle and the 
    # borders must be large enough, otherwise the player loses
    # the game
    if upper_river_border.ycor() - playerTurtle.ycor() < safe_distance_from_border:
        gameover("Game Over")
        return #functions like break
    if -lower_river_border.ycor() + playerTurtle.ycor() < safe_distance_from_border:
        gameover("Game Over lol")
        return #functions like break
    # Part 5.2
    # Move the enemies
    # For every enemy in enemies
    for i in range(len(enemies)):
        # 5.2.1. Move the enemy to the right
        enemies[i].forward(enemy_speeds[i])
        # 5.2.2. If the enemy moves out of the screen, move it 
        #    to the left hand side and generate its speed and 
        #    position randomly
        if enemies[i].xcor() - enemy_width/2 > window_width:
            #reset coordinate of crocordile
            x = -(window_width)/2-(enemy_width)/2
            y = random.randint(int(-(river_width-enemy_height)/2), int((river_width-enemy_height)/2))
            enemies[i].goto(x, y)
            enemy_speeds[i]=random.randint(enemy_speed_min, enemy_speed_max)
        # Part 5.3
        # Check collision
        if playerTurtle.distance(enemies[i]) < safe_distance_from_enemy:
            gameover("gameover, you got bitten")
            return
    # Part 3 (3-4 of 4)
    # 3.3. Update the screen
    # 3.4. Schedule an update in 'update_time_interval' milliseconds
    turtle.tracer(True)
    turtle.tracer(False)
    turtle.ontimer(updatescreen, update_time_interval)

"""
    Here is the entry point of the game
    
    First of all, i create turtles for each component
    in the game with turtle.Turtle().
    The components are:
        1. The player turtle
        2. Two big boxes used as borders of the river
        3. Ten enemies
    
    Then we set up the event handler functions for:
        1. The ondrag() handler to handle the player's control
        2. The ontimer() handler to handle timer event for 
           regular screen update

    After all the components are ready, start the game
"""
# Part 1
turtle.setup(window_width, window_height) # Set the window size
turtle.bgcolor("DarkBlue")

# Part 3 (1 of 4)
# 3.1. Turn off the tracer for preparation of the game
turtle.tracer(False)

# Part 4.1
# 4.1.1. Create the big boxes for upper border and lower border
upper_river_border = turtle.Turtle()
upper_river_border.up()
lower_river_border = turtle.Turtle()
lower_river_border.up()

# 4.1.2. Set the shape of the borders to "square"
upper_river_border.shape("square")
lower_river_border.shape("square")

# 4.1.3. Set the colour of the borders to "DarkOrange4"
upper_river_border.color("DarkOrange4")
lower_river_border.color("DarkOrange4")

# 4.1.4. Set the size of the borders
upper_river_border.shapesize(30, 40)#refer to (y)height and (x)width)
lower_river_border.shapesize(30, 40)

# 4.1.5. Set the initial y position of the borders
upper_river_border.sety((border_height + river_width) / 2)
# 600/2 + 400/2, center of box to center of river
lower_river_border.sety(-(border_height + river_width) / 2)

# Part 5.1
# Add the crocodile image to the pool of shapes
turtle.addshape("crocodile.gif") # Add the image to the turtle system

# Create ten enemies
for _ in range(total_number_of_enemies):

    # a. Create a new turtle 
    enemy = turtle.Turtle()

    # b. Set the shape
    enemy.shape("crocodile.gif") # Use the image for an actual turtle

    # c. Place the crocodile (enemy) in the left hand side randomly
    enemy.up()
    #xposition is at the far left end of the screen
    x = -(window_width + enemy_width) / 2
    #randomise the y position of the crocodile from the borders of the river
    y = random.randint(-(river_width-enemy_height)/2, (river_width-enemy_height)/2)
    enemy.goto(x, y)

    # d. Add the new crocodile (enemy) to the list 'enemies'
    enemies.append(enemy)

    # 5.1.2. Generate a random speed and store it in 'enemy_speeds'
    enemy_speeds.append(random.randint(enemy_speed_min, enemy_speed_max))

# Prepare the player turtle
playerTurtle = turtle.Turtle()
playerTurtle.shape("turtle")
playerTurtle.left(180)
playerTurtle.color("GreenYellow")
playerTurtle.up()

# Part 2 (1 of 2)
# 2.1 Set up event handler functions
#    The event handler function for turtle_name.ondrag()
playerTurtle.ondrag(moveplayerturtle)
# Part 3 (2 of 4)
# The event handler function for turtle.ontimer()
# 3.2. Schedule the first update
#    It starts the main loop and starts the game
turtle.ontimer(updatescreen, update_time_interval)
turtle.tracer(True)
turtle.tracer(False) 

turtle.done()
