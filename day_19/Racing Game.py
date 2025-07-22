import turtle
from turtle import Turtle, Screen
import random
screen = Screen()
user_bet = screen.textinput("Make your bet","Which turtle will win the race?")
screen.setup(width=500,height=400)

is_race_on = False

colors = ['red', 'orange', 'yellow', 'green', 'blue','violet']
all_turtles = []

for turtle_index in range(0,5):
   new_turtle = Turtle(shape="turtle")
   new_turtle.color(colors[turtle_index])
   new_turtle.penup()
   new_turtle.goto(x=-230,y=100-turtle_index*50)
   all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color ==  user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")


screen.exitonclick()
