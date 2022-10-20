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
turtle.tracer(10)

STRLEN = 8
cellSize = 18
rule30 = [0, 1, 1, 1, 1, 0, 0, 0]
initStr = [0, 0, 1, 1, 0, 0, 0, 0]
currentStr = initStr

def square(x, y):
    t.goto(x, y)
    t.setheading(0)
    t.begin_fill()
    for i in range(4):
        t.forward(cellSize-2)
        t.left(90)
    t.end_fill()

def draw(level, currentStr):
    for j in range(STRLEN):
        if currentStr[j]:
            square(level * cellSize - 400, j * cellSize)

def nextStr(inputStr):
    secondStr = [0] * STRLEN
    tri = []
    splitter = 0
    ruleIndex = 0
    for i in range(STRLEN):
        splitter = (i-1)%STRLEN
        tri = inputStr[splitter:] + inputStr[:splitter]
        tri = tri[:3]
        ruleIndex = int("".join(str(x) for x in tri), 2)
        if rule30[ruleIndex]:
            secondStr[i] = 1
    #   print("secondString = ", secondStr)
    return(secondStr)

for i in range(100):
    currentStr = nextStr(currentStr)
    draw(i, currentStr)

turtle.done()
