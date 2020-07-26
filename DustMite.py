# A cool expanding Dust Mite

import turtle
from turtle import Screen
# set window size
width = 1920
height = 1080


screen = Screen()
# current screen setup
screen.setup(width, height)

dustMite = turtle.Turtle()

window = turtle.Screen()

window.bgcolor("indigo")

dustMite.pencolor("pale violet red")

x = 0

y = 0

# dustMite render speed
dustMite.speed(0)
dustMite.penup()
dustMite.goto(0, 200)
dustMite.pendown()

while True:
    dustMite.forward(x)
    dustMite.right(y)
    x += 3
    y += 1
    if y == 1024:
        break
    dustMite.hideturtle()

turtle.done()
