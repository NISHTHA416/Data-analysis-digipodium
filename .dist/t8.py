from turtle import *

def draw_decagon(side_length):
    for _ in range(10):
        forward(side_length)
        right(36)

# Create a turtle object
t = Turtle()

# Set the speed of the turtle
t.speed('fastest')

# Set the pen color and fill color
t.pencolor('blue')
t.fillcolor('yellow')

# Begin filling the decagon with the fill color
t.begin_fill()

# Draw a decagon with a side length of 100 units
draw_decagon(100)

# End filling the decagon
t.end_fill()

# Hide the turtle
t.hideturtle()

# Exit on click
exitonclick()
