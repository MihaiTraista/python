# https://www.youtube.com/watch?v=M_pkidxeGMY

import turtle
import math

turtle.colormode(255)
screen = turtle.Screen()
screen.setup(width=1000, height=1000)
screen.bgcolor(0, 20, 30)
t = turtle.Turtle()
t.speed(0)
t.penup()
t.shape("turtle")
t.color("orange")
t.hideturtle()
turtle.tracer(30)

STRLEN = 40
cellSize = 18
initStr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
currentStr = initStr
rule = []

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
            square(level * cellSize - 400, j * cellSize - 400)

def makeRule(seed):
    rule = bin(seed)
    rule = list(rule)
    rule = rule[2:]
    rule.reverse()
    for i in range(len(rule), STRLEN):
        rule.append('0')
    for i in range(len(rule)):
        rule[i] = int(rule[i])
    return rule

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
        if rule[ruleIndex]:
            secondStr[i] = 1
    #   print("secondString = ", secondStr)
    return(secondStr)

#   MAIN CODE

rule = makeRule(22)     #   try 30, 56, 23, 2, 5, 88, 91, 12, 1, 22!, 57!, 214!
for i in range(50):
    currentStr = nextStr(currentStr)
    draw(i, currentStr)

turtle.done()
