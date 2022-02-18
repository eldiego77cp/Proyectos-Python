import turtle
from turtle import Turtle, Shape, Screen

# Canvas
screen = Screen()
screen.bgcolor('white')

# Turtles

numPlayers = 3

t_1 = Turtle()
t_2 = Turtle()
t_3 = Turtle()

t_1.shape("turtle")
t_1.color("red")
t_2.shape("turtle")
t_2.color("green")
t_3.shape("turtle")
t_3.color("blue")

# Turtle initial position

t_1.penup()
t_1.setpos(0,200)
t_2.penup()
t_2.setpos(0,0)
t_3.penup()
t_3.setpos(0,-200)

# Moves
''' Draw a rectangle'''

t_1.pendown()
t_1.forward(100)
t_1.left(90)
t_1.forward(50)
t_1.left(90)
t_1.forward(100)
t_1.left(90)
t_1.forward(50)
t_1.left(90)

''' Draw a triangle'''

t_2.pendown()
t_2.forward(200)
t_2.left(135)
t_2.forward(150)
t_2.left(90)
t_2.forward(150)
t_2.left(135)

''' Draw a rectangle'''

counter = 0

for i in range (4):
    t_3.forward(20)
    t_3.pendown()
    t_3.forward(80)
    t_3.penup()
    t_3.forward(20)
    t_3.left(90)
    counter =+ 1

turtle.done()