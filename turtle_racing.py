"""
This is a turtle race for 6 separate turtles. A new turtle is
created for each of the racer using turtle.Turtle(). They are stored in a list
and are moved in a random manner.
"""

import turtle
import random
import time

finished = False

# Draw the finishing line using the default turtle
def drawline():
    turtle.tracer(False)
    turtle.up()
    turtle.goto(200, 150)
    turtle.down()


    for _ in range(2):
        turtle.forward(30)
        turtle.right(90)
        turtle.forward(300)
        turtle.right(90)

    for col in range(3):
        for row in range(30):
            if row % 2 == col % 2:
                turtle.begin_fill()
                for _ in range(4):
                    turtle.forward(10)
                    turtle.right(90)
                turtle.end_fill()
            turtle.up()

            # sety() sets the y position of a turtle
            turtle.sety(turtle.ycor() - 10)
            turtle.down()
        
        turtle.up()
        turtle.goto(turtle.xcor() + 10, turtle.ycor() + 300)
        turtle.down()
    turtle.tracer(True)

# Create a new turtle instance for our turtle racer
def createturtle(color, x, y):
    t = turtle.Turtle()
    t.shape("turtle")       # Change to "turtle" shape
    t.fillcolor(color)      # Set the color of the turtle
    t.shapesize(2, 2, 2)    # Make the turtle twice as big
    t.up()
    t.goto(x, y)            # Goto the initial position
    t.down()
    turtles.append(t)       # Append it to the racer list

# Move a random turtle in a random distance
def moveturtle():
    global finished
    
    # Pick a turtle randomly
    index = random.randint(0, 5)

    # Move the turtle randomly
    turtles[index].forward(random.randint(50, 200))
    
    # Check the finishing condition of the race
    x = turtles[index].xcor()
    if x > 200:
        #turtle.tracer(False)
        turtles[index].up()
        turtles[index].forward(50)
        turtles[index].write("Win!")
        turtles[index].backward(50)
        turtles[index].down()
        #turtle.tracer(True)
        print("Turtle", index, "has won the race!")

        # The race has finished
        finished = True

turtle.shape("turtle")

# Draw the finishing line
drawline()
turtle.hideturtle()

# A list to store our turtle racers
turtles = []

# Create the turtle racers with different colours
createturtle("red", -200, 125)
createturtle("green", -200, 75)
createturtle("blue", -200, 25)
createturtle("yellow", -200, -25)
createturtle("cyan", -200, -75)
createturtle("magenta", -200, -125)

# Start the race
while not finished:
    # Move a turtle
    moveturtle()

    # Wait for a random time
    time.sleep(random.randint(100, 1000) / 1000)

turtle.done()
