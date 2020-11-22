"""
In this game the player has to click on the screen.
Then he/she has to click a second time. A circle is
shown which is proportional to the time between clicks.
The circle is not allowed to grow larger than the size
of the previously drawn circle, so the player has to click
the second time when he/she thinks the size of the invisible
circle is getting close to the size of the previous circle.
If the circle drawn by the player is too big, the game is over.
The objective is to draw as many circles as possible.
"""

import turtle
import time

# This is updated every time a new circle is
# successfully added by the player.
current_maximum_radius = 200    

# The number of circles drawn by the player so far
number_of_drawn_circles = 0



def show_instructions_and_outer_circle():

    # Show the title
    turtle.color("blue")
    turtle.goto(0, -290)
    turtle.write("Circles Game", align="center")

    # Show the instructions
    turtle.color("purple")
    turtle.goto(-380, -60)
    turtle.write("""
    1. Click on the screen.
    2. Wait some time.
    3. Click a second time. A circle will be shown.
    4. The longer the time between clicks, the bigger the circle.
        Try to have a duration between clicks so that your circle
        is just smaller than the surrounding circle.
    5. However, you won't be able to see your circle
        until you click the second time!
    6. Try to generate as many as circles as you can.""")

    # Show the first 'maximum size permitted' circle
    show_one_circle(current_maximum_radius, "green", 5)

    # Update the screen display
    turtle.tracer(True) # Update the display
    turtle.tracer(False) # From now onwards, don't update the display


def show_one_circle(radius, color, pensize):
    """
    Draw a single circle of radius 'radius'
    which has a centre at the middle of the screen
    """

    turtle.color(color)
    turtle.pensize(pensize)

    # Draw the circle 
    turtle.goto(0, -radius)
    turtle.down()
    turtle.circle(radius)
    turtle.up()

    # Update the screen display
    turtle.tracer(True) # Update the display
    turtle.tracer(False) # From now onwards, don't update the display

def start_game():
    """
    Get ready to play the game by
    showing the instructions and
    setting up the event handler
    """

    # Show the instructions and outer circle
    show_instructions_and_outer_circle()

    # Set up the event handler for when the
    # user clicks on the screen the first time
    turtle.onscreenclick(first_click)


def first_click(x, y):
    """
    This function is executed when the user
    clicks on the screen the first time.
    """

    global start_time 

    print("First click!")

    # Remember the current time, in seconds
    start_time = time.time()

    # Set up the event handler for when the
    # user clicks on the screen the second time
    turtle.onscreenclick(second_click)


def second_click(x, y):
    """
    This function is executed when the user 
    clicks on the screen the second time. We check  
    whether the radius of the circle is smaller than 
    the permitted maximum radius. If it is, 
    we show the new circle and continue as before.
    If it isn't, we show a 'game over' message and stop.
    """

    global current_maximum_radius, number_of_drawn_circles

    # Turn off any more event handling
    turtle.onscreenclick(None)

    print("Second click!")

    # Remember the current time, in seconds
    end_time = time.time()
    print(end_time)
    # Work out how many seconds have passed between the two clicks
    duration = end_time - start_time
    
    # Show a message which is useful for understanding
    print("Time between clicks=", duration, "seconds")

    current_radius = int( duration * 40 ) 
  
    if current_radius < current_maximum_radius:

        # Draw the circle the user has created    
        show_one_circle(current_radius, "orange", 3)

        current_maximum_radius = current_radius

        number_of_drawn_circles += 1
        #circile becomes the biggest circle and run the time again
        turtle.onscreenclick(first_click)

    # If the circle is bigger than the 
    # previous one we have a game over situation:
    else:
        turtle.color("brown")
        turtle.goto(0, 250)
        turtle.write(
          "Your circle is too big! You have managed to add " +
          str(number_of_drawn_circles) + " circle(s).",
          align="center")
    
        # Show the circle the user created in red
        # to emphasise that it is a 'losing' circle
        show_one_circle(current_radius, "red", 3)


# This is the main part of the program

# Set the turtle window size
turtle.setup(840, 600)

# For this game, we will start by 
# hiding all turtle activity
turtle.tracer(False) 
turtle.up()
turtle.hideturtle()

# Start the game
start_game()

# Wait for any events and handle them
turtle.done()
