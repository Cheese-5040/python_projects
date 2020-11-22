#Done by OW YONG, Chee Seng SID: 2065 9467
import turtle
print("Done by OW YONG, Chee Seng, SID:20659467")
turtle.width(4)
turtle.speed(0)

print("welcome to python sketchbook")
fill_color="none"
option = ""

while option != "q":
  
    print()
    print("please enter one of the following options")
    print()
    print("m - Move the turtle")
    print("t - Rotate the turtle")
    
    print("l - Draw a line")
    print("r - Draw a rectangle")
    
    print("c - Draw a circle")
    print("p - Change pen colour of the turtle")
    print("f - Change the fill colour of the turtle")
    print("g - Draw a generated flower")
    print("e - Draw a generated explosion")
    print("q - Quit the program")
    print()
    option = str(input("please input your option?"))
  
    if option == "m":
        #move the turtle
        x=int(input("please enter the x location:"))
        y=int(input("please enter the y location:"))
        turtle.up()
        turtle.goto(x,y)
        turtle.down()

    if option == "t":
        #rotate turtle
        a= int(input("please input the angle of rotation"))
        turtle.right(a)

    if option == "l":
        #draw line
        x=int(input("please enter the x location:"))
        y=int(input("please enter the y location:"))
        turtle.goto(x,y)

    if option == "r":
        #draw rectangle
        w=int(input("please enter the width of the rectangle: "))
        h=int(input("please enter the height of the rectangle: "))
        if fill_color != "none":
            turtle.begin_fill()
        #print (fill_color)

        for i in range (0,2):
            turtle.forward(w)
            turtle.left(90)
            turtle.forward(h)
            turtle.left(90)

        if fill_color != "none":
             turtle.end_fill()

    if option == "c":
        #draw circle
        c=int(input("please enter the radius of the circle: "))
        if fill_color != "none":
            turtle.begin_fill()

        #print(fill_color)
        turtle.circle(c)

        if fill_color != "none":
             turtle.end_fill()

    if option == "p":
        #pen colour change
        pen_color=str(input("please enter the colour name: "))
        turtle.pencolor(pen_color)


    if option == "f":
        #change fill colour of the turtle
        fill_color=str(input("please enter the fill colour (Type 'none' to clear the color):"))
        if fill_color != "none":
            turtle.fillcolor(fill_color)

            
    if option == "g":
        #draw a generated flower (embedded loop)
        r=int(input("please enter the radius of the flower petal: "))
      
        if fill_color != "none":
            turtle.begin_fill()
        for j in range (0,20):
            for i in range (0,4):
                turtle.circle(r,180)
                turtle.left(360/4)
            turtle.left(360/20)
        if fill_color != "none":
            turtle.end_fill()


    if option == "e":
        #draw a generated explosion
        s= int(input("please enter the size of the explosion(>150):"))
        for thiscolor in ["MediumPurple", "OrangeRed", "goldenRod","yellow"]:
            for i in range (1,5):
                newcolor=thiscolor+str(i)
                turtle.color(newcolor)
                turtle.dot(s)
                s=s-10
                
            
turtle.done()
        
