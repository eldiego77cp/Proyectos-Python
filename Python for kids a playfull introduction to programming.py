'''
Programming Puzzles
The following are a few experiments you can try yourself. The
answers can be found at http://python-for-kids.com/.

#1: Favorites
Make a list of your favorite hobbies and give the list the variable
name games. Now make a list of your favorite foods and name the
variable foods. Join the two lists and name the result favorites.
Finally, print the variable favorites.

#2: Counting Combatants
If there are 3 buildings with 25 ninjas hiding on each roof and
2 tunnels with 40 samurai hiding inside each tunnel, how many
ninjas and samurai are about to do battle? (You can do this with
one equation in the Python shell.)

#3: Greetings!
Create two variables: one that points to your first name and
one that points to your last name. Now create a string and use
placeholders to print your name with a message using those two
variables, such as “Hi there, Brando Ickett!”
'''

games = ['chess', 'soccer', 'paddle', 'programming', 'fixing']
foods = ['milanesa', 'french fries', 'asado', 'pizza']
favorites = games + foods
print(favorites)

buildings = 3
ninjas = 25
tunnels = 2
samurais = 40

combatants = buildings * ninjas + tunnels * samurais
print(combatants)

nombre = 'Alejandro'
apellido = 'Fernandez'
message = 'Hi there, %s %s!'

print(message % (nombre, apellido))

'''
Programming Puzzles
Try drawing some of the following shapes with the turtle. The
answers can be found at http://python-for-kids.com/.

#1: A Rectangle
Create a new canvas using the turtle module’s Pen function and
then draw a rectangle.

#2: A Triangle
Create another canvas, and this time, draw a triangle. Look back
at the diagram of the circle with the degrees (“Moving the Turtle”
on page 46) to remind yourself which direction to turn the turtle
using degrees.

#3: A Box Without Corners
Write a program to draw the four lines shown here (the size isn’t
important, just the shape):

'''

import turtle

# Canvas
screen = turtle.Screen()
screen.bgcolor("white")

# Turtles

t_1 = turtle.Turtle()
t_2 = turtle.Turtle()
t_3 = turtle.Turtle()

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

# turtle.done()

'''
Programming Puzzles
Try the following puzzles using if statement and conditions. The
answers can be found at http://python-for-kids.com/.

#1: Are You Rich?
What do you think the following code will do? Try to figure out
the answer without typing it into the shell, and then check your
answer.

>>> money = 2000
>>> if money > 1000:
print("I'm rich!!")
else:
print("I'm not rich!!")
print("But I might be later...")

#2: Twinkies!
Create an if statement that checks whether a number of Twinkies
(in the variable twinkies) is less than 100 or greater than 500. Your
program should print the message “Too few or too many” if the
condition is true.

#3: Just the Right Number
Create an if statement that checks whether the amount of money
contained in the variable money is between 100 and 500 or between
1,000 and 5,000.

#4: I Can Fight Those Ninjas
Create an if statement that prints the string “That’s too many”
if the variable ninjas contains a number that’s less than 50, prints
“It’ll be a struggle, but I can take ’em” if it’s less than 30, and
prints “I can fight those ninjas!” if it’s less than 10. You might
try out your code with:
>>> ninjas = 5

'''

money = 2000
if money > 1000:
    print("I'm rich!!")
else:
    print("I'm not rich!!")
    print("But I might be later...")

twinkies = 90
if twinkies < 100 or twinkies > 500:
    print("Too few or too many")

money = 600
if (money > 100 and money < 500) or (money > 1000 and money < 5000):
    print("true")
else: 
    print("false")

ninjas = 45
if ninjas < 10: 
    print("I can fight those ninjas!")
elif ninjas < 30:
    print("It 'll be a struggle, but I can take 'em")
elif ninjas < 50:
    print("That's too many")