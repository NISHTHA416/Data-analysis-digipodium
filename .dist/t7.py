from turtle import*

speed('fastest')

sides=5
distance=100
for i in range(sides):
    rt(144)
    fd(distance)
    lt(72)
    fd(distance)
    for i in range(sides):
     rt(144)
     fd(distance)
     lt(72)
     fd(distance)
    
    






    hideturtle()
    mainloop()