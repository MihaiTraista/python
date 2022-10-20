import turtle
import math
import random

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
turtle.tracer(50)

levels = 2

currentColor = [128, 128, 128]

# comment
def slightRandColor(amount):
  currentColor[0] = (currentColor[0] + random.randint(amount*-1, amount)) % 255
  currentColor[1] = (currentColor[1] + random.randint(amount*-1, amount)) % 255
  currentColor[2] = (currentColor[2] + random.randint(amount*-1, amount)) % 255
  t.color(tuple(currentColor))


def rotate(initX, initY, radius, angle):
    rad = math.radians(angle)
    newX = (math.sin(rad) * radius) * (initX / radius)
    newY = (math.cos(rad) * radius) * (initX / radius)
    rad = math.radians(90-angle)
    newX -= initY * math.sin(rad)
    newY += initY * math.cos(rad)
    return(newX, newY)

def arch(x, y, length, angle, reverse):
    t.penup()
    t.goto(x, y)
    t.pendown()
    #   x = r(t-sin t)
    #   y = r(1-cos t)
    for i in range(360):
        rad = math.radians(i)
        newX = length * (rad - math.sin(rad))
        newY = length * (1 - math.cos(rad))
        if reverse:
            newY *= -1
        coord = rotate(newX, newY, length, angle)
        newX = coord[0]+x
        newY = coord[1]+y
        t.goto(newX, newY)

def main():
    for i in range(5):
        t.color("orange")
        arch(0, 0, 40, i*(360/5), False)
        secX = t.xcor()
        secY = t.ycor()
        for ii in range(4):
            arch(secX, secY, 10, ii * (360 / 4), False)
            thirdX = t.xcor()
            thirdY = t.ycor()
            slightRandColor(20)
            for iii in range(3):
                arch(thirdX, thirdY, 3, iii * (360 / 3), False)
                fourthX = t.xcor()
                fourthY = t.ycor()
                slightRandColor(20)
                for iiii in range(5):
                    arch(fourthX, fourthY, 1, iiii * (360 / 5), False)
                    arch(fourthX, fourthY, 1, iiii * (360 / 5), True)
                arch(thirdX, thirdY, 3, iii * (360 / 3), True)
            arch(secX, secY, 10, ii * (360 / 4), True)
        arch(0, 0, 40, i*(360/5), True)

main()

turtle.done()
