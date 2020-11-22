import turtle
import random
    
### This part of Python code will create the jigsaw pieces when starting up
### by setting up random positions and loading the corresponding image

def createJigsaw():
    global allTurtles

    # Initialize the variables of total number of rows and columns
    totalRows=4
    totalColumns=4
    # Now we go through the jigsaw piece row-column structure
    # Go through each row
    for row in range (totalRows):
        # Go through each column in this row
        for column in range(totalColumns):
            # Generate a random position
            width=turtle.window_width()
            height=turtle.window_height()
            x=random.randint(-width/2, width/2)
            y=random.randint(-height/2, height/2)
            print(x,y)
            
            # Make a new turtle
            newTurtle=turtle.Turtle()
            newTurtle.up()
            #speed is fastest so that you can get fast response when dragging the image
            newTurtle.speed(0)
            
            # Move it to the random position
            newTurtle.goto(x,y)

            # Build the image file name
            theFilename=str(row)+"-"+str(column)+".gif"
            print(theFilename)
            
            # Add the image to the turtle system
            turtle.addshape("C:\\Users\\Owner\\Desktop\\documents hkust\\sem 2 2020 spring\\COMP 1021\\cut_images_TRiwhzo2T2\\"+theFilename)
            
            # Apply the new image to this turtle
            newTurtle.shape("C:\\Users\\Owner\\Desktop\\documents hkust\\sem 2 2020 spring\\COMP 1021\\cut_images_TRiwhzo2T2\\"+theFilename)
            
            # when drag, go to the place that it is dragged
            newTurtle.ondrag(newTurtle.goto)
            
            # Add the new turtle to the new list of turtles
            allTurtles.append(newTurtle)

        
### This part of Python code will only run when the user presses "c" to check the jigsaw
def checkJigsaw():
    checkResult=True # At the start, we assume everything is OK

    for thisTurtle in allTurtles: # Go through every single turtle that we made
        thisX = thisTurtle.xcor() # x coordinate of this turtle
        thisY = thisTurtle.ycor() # y coordinate of this turtle

        theFilename = thisTurtle.shape() # Take the image filename of this turtle
        
        lengthOfFilenameWithoutExtension= len(theFilename)-4 # How long the filename is without the ".gif"
        theFilenameWithoutExtension=theFilename[ -7: lengthOfFilenameWithoutExtension ] # Remove the ".gif"
        FilenameWithoutExtension=theFilenameWithoutExtension.split("-") # Divide the filename into 3 pieces
        #print(FilenameWithoutExtension)

        thisRow=int(FilenameWithoutExtension[0]) # Take the Row number from the filename (the second piece of text)
        thisCol=int(FilenameWithoutExtension[1]) # Take the Col number from the filename (the third piece of text)
        
        # We need to check this turtle with all other turtles for position violations
        for compareTurtle in allTurtles: # Go through every other turtle
            compareX = compareTurtle.xcor() # Get the x coordinate of the turtle
            compareY = compareTurtle.ycor() # Get the y coordinate of the turtle
            
            compareFilename = compareTurtle.shape() # Take the image filename of this turtle
            
            lengthOfCompareFilenameWithoutExtension= len(compareFilename)-4 # How long the filename is without the ".gif"
            compareFilenameWithoutExtension=compareFilename[-7 : lengthOfCompareFilenameWithoutExtension ] # Remove the ".gif"
            FilenameWithoutExtension=compareFilenameWithoutExtension.split("-") # Divide the filename into 3 pieces
            print(FilenameWithoutExtension)
            compareRow=int(FilenameWithoutExtension[0]) # Take the Row number from the filename (the second piece of text)
            compareCol=int(FilenameWithoutExtension[1]) # Take the Col number from the filename (the third piece of text)
            
            
            # Here, the four position violations will be checked
            # The jigsaw is wrong if any of them fails
            
            # The piece has a smaller column value but is on the right
            if thisCol < compareCol and thisX >= compareX:
                checkResult = False
                break

            # The piece has a larger column value but is on the left
            if thisCol > compareCol and thisX <= compareX:
                checkResult = False
                break
        
            # The piece has a smaller row value but is on the bottom
            if thisRow < compareRow and thisY <= compareY:
                checkResult = False
                break
            # The piece has a larger row value but is on the top
            if thisRow > compareRow and thisY >=compareY:
                checkResult = False
                break
        

            
    # Let's check the final result and show an appropriate message
    if checkResult:
        print("Congratulations! Your jigsaw is correct!")
    else:
        print("Oh no! Your jigsaw is WRONG!!")

### Here is the main part of the program

allTurtles=[] # We will store all the turtles in this list

createJigsaw() # Create the jigsaw pieces
    
turtle.onkeypress(checkJigsaw, "c") # Press 'c' whenever you want to check the jigsaw

turtle.listen() # Listen for key presses

### Note: turtle.mainloop() is exactly the same as turtle.done()
turtle.mainloop() # Keep checking if anything is happening, if so do something appropriate

