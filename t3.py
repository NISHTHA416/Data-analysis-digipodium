from turtle import*

speed('fastest')

#polygon

distance = 100
sides = 10

for i in range(sides):
    #froward
    fd(distance)
    rt(360/sides)

    for i in range (sides):
        fd(distance/4)
        lt(360/sides)


    hideturtle()
    mainloop()# this line is needed to keep the window open   







