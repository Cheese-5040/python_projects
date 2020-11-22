#using multiple turtles
import turtle
import time
import random
turtles=[]
finished = False
turtle.up()
turtle.goto(200,200)
turtle.down()
turtle.right(90)
turtle.forward(200)
def createturtle(colour,x,y):
    t=turtle.Turtle()#line to create new turtle
    t.up()
    t.shape("turtle")#shape of turtle
    t.color("grey",colour)
    t.shapesize(1,2,2)#change shape of turtle to y-width, x-length, outline
    turtles.append(t)#add to list of turtles
    t.goto(x,y)
    
createturtle("red",-200,150)
createturtle("blue",-200,100)
createturtle("yellow",-200,50)

def moveturtle():
    global finished
    index=random.randint(0,2) #pick random turtle
    turtles[index].forward(random.randint(50,100))# move forward rand distance
    x=turtles[index].xcor()
    if x>200:
        finished= True
        turtles[index].write("win",font=("ariel",14,"bold"),align="center")#write on turtle window

while not finished:
    moveturtle()
    time.sleep(random.randint(100,1000)/1000)#random time to move from 0.1 to 1s
    
    
turtle.done()
