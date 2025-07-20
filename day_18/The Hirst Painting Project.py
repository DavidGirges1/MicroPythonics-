import random
import colorgram
from turtle import Turtle, Screen, colormode

colormode(255)

# Extract 15 colors from the image
colors = colorgram.extract('paint.jpg', 15)
colors_rgb = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]

# Turtle setup
tim = Turtle()
tim.speed('fastest')
tim.hideturtle()
tim.penup()

# Screen setup
screen = Screen()
screen.setup(width=300, height=300)  # Set window size

# Starting position
start_x = -250
start_y = 250
tim.teleport(start_x, start_y)

# Grid dimensions
num_rows = 10
num_cols =  10
dot_spacing = 50
for row in range(num_rows):
    for col in range(num_cols):
        random_color = random.choice(colors_rgb)
        tim.dot(20, random_color)

        tim.forward(dot_spacing)

    # Move to the next row
    new_y = start_y - (row + 1) * dot_spacing
    tim.teleport(start_x, new_y)



screen.exitonclick()

