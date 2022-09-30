#importing libraries
import turtle
import time

from turtle import Turtle
from random import randint

# window and screen setup
sc = turtle.Screen()
tr = Turtle()
sc.setup(width = 1360,height = 768)
sc.bgcolor("forestgreen")
turtle.color("white")
turtle.speed(0)
turtle.up()
turtle.shape("turtle")
turtle.title("Turtle Game")
#Showing the name at upper left corner
turtle.goto(0,240)
font =("arial",30,"bold")
turtle.color("cyan")
turtle.write("TURTLE RACE",font = font, align ="center")
turtle.up()

#set up the dirt
turtle.goto(-700,-290)
turtle.color("chocolate")
turtle.begin_fill()
turtle.down()
turtle.fd(1500)
turtle.rt(90)
turtle.fd(60)
turtle.rt(90)
turtle.fd(1500)
turtle.rt(90)
turtle.fd(60)
turtle.end_fill()

#set up finish line
square_size = 15
finish_line = 650

turtle.color("black")
turtle.shape("square")
turtle.up()

for i in range(15):
    turtle.goto(finish_line,(140 - (i*square_size*2)))
    turtle.stamp()
for j in range(14):
    turtle.goto(finish_line+square_size,((140 - square_size) - (j*square_size*2)))
    turtle.stamp()
  
turtle.hideturtle()

#Creating different turtles
start_x = -580

myTurtle1 = Turtle()
myTurtle1.speed(0)
myTurtle1.color("red")
myTurtle1.shape("turtle")
myTurtle1.shapesize(2,2,2)
myTurtle1.up()
myTurtle1.goto(start_x,100)

myTurtle2 = Turtle()
myTurtle2.speed(0)
myTurtle2.color("yellow")
myTurtle2.shape("turtle")
myTurtle2.shapesize(2,2,2)
myTurtle2.up()
myTurtle2.goto(start_x,0)

myTurtle3 = Turtle()
myTurtle3.speed(0)
myTurtle3.color("purple")
myTurtle3.shape("turtle")
myTurtle3.shapesize(2,2,2)
myTurtle3.up()
myTurtle3.goto(start_x,-100)

myTurtle4 = Turtle()
myTurtle4.speed(0)
myTurtle4.color("violet")
myTurtle4.shape("turtle")
myTurtle4.shapesize(2,2,2)
myTurtle4.up()
myTurtle4.goto(start_x,-200)

time.sleep(1)

#Movement of turtles
for i in range(150):
    myTurtle1.fd(randint(1,15))
    myTurtle2.fd(randint(1,15))
    myTurtle3.fd(randint(1,15))
    myTurtle4.fd(randint(1,15))

#Show the winner on screen
x1 = myTurtle1.xcor()
x2 = myTurtle2.xcor()
x3 = myTurtle3.xcor()
x4 = myTurtle4.xcor()

turtle.goto(0,190)
font_size = 30
alignment = "center"
font =("arial",font_size,"bold")


if x1 > x2 and x1 > x3 and x1 > x4:
  turtle.color("red")
  turtle.write("RED TURTLE IS THE WINNER",font = font, align = alignment)
  
elif x2 > x1 and x2 > x3 and x2 > x4:
  turtle.color("yellow")
  turtle.write("YELLOW TURTLE IS THE WINNER",font = font, align = alignment)
  
elif x3 > x1 and x3 > x2 and x3 > x4:
  turtle.color("purple")
  turtle.write("PURPLE TURTLE IS THE WINNER",font = font, align = alignment)
  
elif x4 > x1 and x4 > x2 and x4 > x3:
  turtle.color("violet")
  turtle.write("VIOLET TURTLE IS THE WINNER",font = font, align = alignment)

time.sleep(10)
turtle.bye()

      
