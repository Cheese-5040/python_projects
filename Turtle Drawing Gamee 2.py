#prepared by: OW YONG, Chee Seng, SID:20659467


import turtle
turtle.setup(800,600) #set the x and y length to be 800 x 600

num_divisions=8 # set number of divisions in the diagram
turtle_width=3# set how thicc the turtle 

#remove animation of turtle
turtle.tracer(False)

#do the background
backgroundTurtle=turtle.Turtle()
backgroundTurtle.width(1)

backgroundTurtle.down()
backgroundTurtle.color("gray88") #drawing the center line in the background

#draw the lines on the background of turtle
for i in range (num_divisions):
    backgroundTurtle.forward(500)
    backgroundTurtle.backward(500)
    backgroundTurtle.left(360/num_divisions)

backgroundTurtle.up()

#display text on turtle window
backgroundTurtle.color("purple")
backgroundTurtle.goto(-turtle.window_width()/2+50, 100)
backgroundTurtle.write("""s - change a colour for one of the colour buttons
m - all 8 drawing turtles go to the middle
c - clear all drawing s made by the 8 drawing turtles
""", font= ("Arial", 14, "normal"))

backgroundTurtle.hideturtle()

#set turtle to handle messege on turtle screen
messageTurtle=turtle.Turtle()
#set colour of text to red
messageTurtle.color("red")
#lift turtle
messageTurtle.up()
# Set it the be at center, near the colour selections
messageTurtle.goto(0, -200)
# We do not want to show it on the screen
messageTurtle.hideturtle()

# Part 2 Preparing the drawing turtles

# The drawing turtles are put in a list
allDrawingTurtles = [] 

# Part 2.1 Add the 8 turtles in the list
for i in range (num_divisions):
    newTurtle = turtle.Turtle()
    #set up
    newTurtle.speed(0)
    newTurtle.width(turtle_width)
    newTurtle.hideturtle()

    allDrawingTurtles.append(newTurtle)

#print(len(allDrawingTurtles))

# Part 2.2 Set up the first turtle for drawing
dragTurtle= allDrawingTurtles[0]
dragTurtle.showturtle()

dragTurtle.shape("circle")
dragTurtle.shapesize(2,2)

# Part 3 Preparing the basic drawing system
# Set up the ondrag event
def draw(x,y):
    dragTurtle.ondrag(None) #disable event
    global messageTurtle
    messageTurtle.clear()
    dragTurtle.goto(x,y)
    
    x_transform=[1,1,-1,-1,1,1,-1,-1]
    y_transform=[1,-1,1,-1,1,-1,1,-1]
    for i in range(1, num_divisions):
        if i < 4:
            new_x = x* x_transform[i] #x with sign change
            new_y = y* y_transform[i] #y with sign change

        else:
            new_x = y* y_transform[i]
            new_y = x* x_transform[i]
        allDrawingTurtles[i].goto(new_x, new_y)
    
    dragTurtle.ondrag(draw) #enable event
dragTurtle.ondrag(draw)

# Part 5.2 clear all drawings made by the 8 drawing turtles
def clearDrawing():
    global messageTurtle#set variable to a global variable
    messageTurtle.clear()
    turtle.listen()

    for j in range (num_divisions):
        turtle.tracer(False) 
        allDrawingTurtles[j].clear()
        turtle.tracer(True)
    
    messageTurtle=turtle.Turtle()
    messageTurtle.hideturtle()
    messageTurtle.color("red")
    messageTurtle.up()
    messageTurtle.goto(0,-200)
    messageTurtle.write("The screen is cleared", align="center", font= ("Arial", 14, "normal"))
turtle.onkeypress(clearDrawing,'c')

# Part 5.3 all 8 drawing turtles go to middle
def goToMiddle():
    global messageTurtle#set variable to a global variable

    messageTurtle.clear()
    turtle.listen()
    messageTurtle.clear()
    for j in range (num_divisions):
        turtle.tracer(False)
        allDrawingTurtles[j].up()
        allDrawingTurtles[j].goto(0,0)#allDrawingTurtles[j].home() also works
        allDrawingTurtles[j].down()
        turtle.tracer(True)
    messageTurtle=turtle.Turtle()
    messageTurtle.hideturtle()
    messageTurtle.color("red")
    messageTurtle.up()
    messageTurtle.goto(0,-200)
    messageTurtle.write("All 8 turtles returned to the middle", align="center", font= ("Arial", 14, "normal"))
   
turtle.onkeypress(goToMiddle, 'm')
# Part 4 handling the colour selection
# Make the colour selection turtles
# Here is the list of colours
colours = ["black", "orange red", "lime", "medium purple", "light sky blue", "orchid", "gold"]

# Part 4.2 Set up the onclick event
def handleColourChange(x,y):
    for i in range(len(colours)):
        if x <= (-130+50*i) and x >= -180+50*i:
            #print("you clicked position: ", i)
            for j in range (num_divisions):
                allDrawingTurtles[j].color(colours[i])
# Part 5.4 change a colour in the colour selection
def changeColour():
    global messageTurtle#set variable to a global variable
    global t
    
    messageTurtle.clear()
    turtle.listen()
    index= turtle.textinput("Change color","Please type the index number for the turtle: (0-6)")

    if index != None:
        index=int(index)

        while index >6 or index <0:
            turtle.listen()
            index= int(turtle.textinput("Change color","Please type the correct index number for the turtle: (0-6)"))

        turtle.listen()
        color= turtle.textinput("Change color","Please type the color you want to use e.g. LightBlue")
        if color != None:
            colours.pop(index)
            colours.insert(index,color)
            for i in range (len(colours)):
                t=turtle.Turtle()
                turtle.tracer(False)
                
                t.shape("square")
                t.shapesize(2,2)
                t.up()
                t.color(colours[i])
                t.goto(-150 +50*i, -250)# y coordinate same but x will be always slighly to the right
                
                t.onclick(handleColourChange)
                colourSelectionTurtles.append(t)
            turtle.tracer(True)
            turtle.listen()
  
            messageTurtle=turtle.Turtle()
            messageTurtle.hideturtle()
            messageTurtle.color("red")
            messageTurtle.up()
            messageTurtle.goto(0,-200)
            messageTurtle.write("The colour for that button has been change\
d, click on the button to use it", align="center", font= ("Arial", 14, "normal"))

    else:
        for i in range (len(colours)):
            t=turtle.Turtle()
            turtle.tracer(False)
                
            t.shape("square")
            t.shapesize(2,2)
            t.up()
            t.color(colours[i])
            t.goto(-150 +50*i, -250)# y coordinate same but x will be always slighly to the right
                
            t.onclick(handleColourChange)
            colourSelectionTurtles.append(t)
        turtle.tracer(True)
        turtle.listen()
turtle.onkeypress(changeColour,'s')

# Part 4.1 Make the colour selection turtles
colourSelectionTurtles = []

for i in range(len(colours)):
    global t
    t=turtle.Turtle()
    t.shape("square")
    t.shapesize(2,2)
    t.up()
    t.color(colours[i])
    t.goto(-150 +50*i, -250)# y coordinate same but x will be always slighly to the right
    t.onclick(handleColourChange)
    colourSelectionTurtles.append(t)

turtle.tracer(True)
turtle.listen()

turtle.done()

