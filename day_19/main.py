# drawomg npard challenge
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

tim.color(r"blue")
tim.shape("arrow")

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def clockwise():
    tim.right(10)
def counter_clockwise():
    tim.left(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="w",fun= move_forward)
screen.onkey(fun=move_backward,key="s")
screen.onkey(fun=clockwise,key="d")
screen.onkey(fun=counter_clockwise,key="a")
screen.onkey(fun=clear,key="c")
screen.exitonclickwwwww()

























