import turtle
import random

# Setup the screen
win = turtle.Screen()
win.setup(width=800, height=600)
win.bgcolor('black')
win.title("Good Night Scene")

# Color options
colors = ['white', 'yellow', 'cyan', 'lightblue']

# Moon turtle
moon = turtle.Turtle()
moon.hideturtle()
moon.speed(10)  # Fast, animated

# Star turtle
star = turtle.Turtle()
star.hideturtle()
star.speed(0)  # Fast, animated

# Text turtle
text = turtle.Turtle()
text.hideturtle()
text.speed(10)

# Draw the moon
def draw_moon(pos, color):
    x, y = pos
    moon.penup()
    moon.goto(x, y)
    moon.color(color)
    moon.begin_fill()
    moon.circle(50)
    moon.end_fill()

# Draw random stars
def draw_stars(count):
    for _ in range(count):
        x = random.randint(-390, 390)
        y = random.randint(-290, 290)
        size = random.randint(2, 5)
        color = random.choice(colors)
        
        star.penup()
        star.goto(x, y)
        star.dot(size, color)
        
# Display "Good Night" text
def write_text():
    text.penup()
    text.goto(0, -250)
    text.color('white')
    text.write("Good Night", align="center", font=("Segoe Script", 32, "bold"))

# Draw the scene
draw_stars(100)
draw_moon((250, 180), 'white')
write_text()

# Keep window open
turtle.done()
