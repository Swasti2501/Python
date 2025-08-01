import turtle as r

r.bgcolor("black")
r.pencolor("lavender")
r.title("Flower")
r.speed(0)
r.width(3)

def form(x):
    r.circle(100, x)
    r.penup()
    r.goto(0, 0)
    r.pendown()
    r.circle(-100, x)

def leaf():
    for angle in [0, 90, 180, 270]:  
        r.setheading(angle)
        for i in range(0, 140, 10):
            form(i)

leaf()

r.exitonclick()
r.done()
