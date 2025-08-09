import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("NIGHT NIGHT")

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.color("white")

def draw_moon(x, y, radius, color1, color2):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(color1)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()

    pen.penup()
    pen.goto(x + radius/3, y + radius/3)
    pen.pendown()
    pen.color(color2)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()

def draw_star(x, y, size, color):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(color)
    pen.begin_fill()
    for i in range(10):
        pen.forward(size)
        pen.right(144)
    pen.end_fill()

def display_slanted_text(message, x, y, font_size, color, angle):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(color)
    pen.setheading(angle)
    pen.write(message, align="center", font=("Times New Roman", font_size, "bold"))
    pen.setheading(0)
    
def display_infinity(message, x, y, font_size, color):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(color)
    pen.write(message, align="center", font=("Times New Roman", font_size, "bold"))
    
    
draw_moon(-50, 100, 50, "white", "black")

stars = [(-150, 200), (100, 150), (-100, 250), (150, 250), (-200, 100), (200, 100), (-150, 50), (100, 50), (150, 150)]
for star in stars:
    draw_star(star[0], star[1], 20, "yellow")

display_slanted_text("NIGHT NIGHT", 0, -50, 36, "white", 60)


pen.hideturtle()
screen.mainloop()
