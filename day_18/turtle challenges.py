# working more with turtle
import time
import turtle
import turtle as t
from turtle import Turtle, Screen
import random

timy = Turtle()
timy.shape("turtle")
timy.color("firebrick4")
t.colormode(255)

# challenge 1: Draw a square
for _ in range(4):
    timy.forward(100)
    timy.right(90)


# challenge 2: draw a dashed line
for _ in range(10 ):
    timy.forward(10)
    timy.penup()
    timy.forward(10)
    timy.pendown()

# challenge 3: wrie a triangle, square .... decagon
colors = [
    "red", "blue", "green", "orange", "purple", "yellow", "brown", "pink", "gray"
]


for  x in range(3,10):
    for _ in range(x):
        timy.forward(100)
        timy.right(360/x)
    timy.color(random.choice(colors))
#
#

# Challenge 4: drawing a random walk
timy.pensize(10)
timy.hideturtle()
timy.speed("fastest")
direction = [0,90,180,270]
# color = ["red", "blue", "green", "orange", "purple", "yellow", "brown", "pink", "gray"]


for _ in range(200):
    timy.color(random.randint(0,255) ,random.randint(0,255),random.randint(0,255) )
    timy.forward(20)
    dir = random.choice(direction)
    timy.setheading(random.choice(direction))

# challenge 5: make a spriograph
timy.speed("fastest")
timy.hideturtle()

def draw_spirograph(size_of_gap):
    for _ in range(int(360//size_of_gap)):
        timy.color(random.randint(0,255) ,random.randint(0,255),random.randint(0,255) )
        timy.circle(100)
        timy.setheading(timy.heading()+size_of_gap)

draw_spirograph(5)

screen = Screen()
screen.exitonclick()
































