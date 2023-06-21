from turtle import*

speed('fastest')

#polygon
distance =100
side =6

for i in range (side):
    pencolor('red')
    fd(distance)
    rt(360/side)
    
    for i in range(side):
        pencolor('blue')
        fd(distance/2)
        rt(360/side)
        dot(10)
        write(i)
        
        hideturtle()
        mainloop 
