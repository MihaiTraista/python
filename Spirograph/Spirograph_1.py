# doesn't work last tried 6Sep. I need to watch the Khan academy videos

import turtle
import math

turtle.colormode(255)
screen = turtle.Screen()
screen.setup(width=1000, height=1000)
screen.bgcolor(0, 40, 50)
t = turtle.Turtle()
t.speed(0)
t.penup()
t.shape("turtle")
t.color("orange")
t.hideturtle()
turtle.tracer(20)

radius = 200

def rotate(initX, initY, radius, angle):
    rad = math.radians(angle)
    newX = (math.sin(rad) * radius) * (initX / radius)
    newY = (math.cos(rad) * radius) * (initX / radius)
    rad = math.radians(90-angle)
    newX -= initY * math.sin(rad)
    newY += initY * math.cos(rad)
    return(newX, newY)

def arc(x, y, radius, angle):
    t.penup()
    t.goto(x, y)
    t.pendown()
    for i in range(radius):
        newX = i
        newY = math.sin((i/radius) * math.pi * 2) * 50
        newX += x
        newY += y
        t.goto(rotate(newX, newY, 200, angle))

for i in range(12):
    arc(0, 0, radius, i*(360/12))

turtle.done()
