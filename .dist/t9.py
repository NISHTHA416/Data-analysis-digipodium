from turtle import *

# Set the speed of the turtle
speed('fastest')

# Set the number of points for the star
points = 5

# Set the length of each side
side_length = 100

# Calculate the angle for each turn
angle = 180 - (180 / points)

# Draw the star
for _ in range(points):
    forward(side_length)
    right(angle * 2)

# Hide the turtle cursor and keep the window open
hideturtle()
mainloop()
