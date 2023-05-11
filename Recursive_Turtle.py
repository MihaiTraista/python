import turtle
import math
import random

# define turtle object
t = turtle.Turtle()
screen = turtle.Screen()
screen.setup(900, 900)
t.shape("turtle")
t.speed(0)

# prepare for drawing
t.color("orange")
turtle.colormode(255)
screen.bgcolor(15, 15, 15)
turtle.tracer(19)
t.penup()
t.goto(-50, -100)
t.pendown()

currentColor = [128, 128, 128]


turtle.done()