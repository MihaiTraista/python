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
turtle.tracer(12)

levels = 2

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
        newY = math.sin((i/radius) * math.pi * 2) * radius/4
        coord = rotate(newX, newY, radius, angle)
        newX = coord[0]+x
        newY = coord[1]+y
        t.goto(newX, newY)

def spiro(arcCount, centreX, centreY, radius):
    global levels
    for i in range(arcCount):
        arc(centreX, centreY, radius, i*(360/arcCount))
        newX = t.xcor()
        newY = t.ycor()
        for ii in range(arcCount):
            arc(newX, newY, int(radius/6), ii*(360/arcCount))


def main():
    spiro(12, 0, 0, 200)

main()

turtle.done()
