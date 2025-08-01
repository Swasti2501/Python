import math
import turtle

def x(t):
    return 16*math.sin(t)**3
def y(t):
    return 13*math.cos(t)-5*\
        math.cos(2*t)-2*\
            math.cos(3*t)-\
                math.cos(4*t)
                
t = turtle.Turtle()
t.speed(9)
turtle.bgcolor("black")

for i in range(380):
    t.goto((x(i)*10,y(i)*10))
    t.pencolor("red")
    t.goto(0,0)
    
turtle.exitonclick()

    
                    