#   tried to use objects but I don't see any benefit. The method move() shouldn't be
#   inside the object because it's suppore to interact with other objects

import turtle
import math

turtle.colormode(255)
screen = turtle.Screen()
screen.setup(width=900, height=900)
screen.bgcolor(0, 0, 0)
t = turtle.Turtle()
t.speed(0)
t.penup()
t.shape("turtle")
#   t.hideturtle()
turtle.tracer(10)


class Pawn:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.selected = False

    def move(self, occupied, moveToX, moveToY):
        self.isForward = True if  moveToX == self.x and moveToY == self.y+1 else False
        self.isDiagonal = True if moveToY != self.y and moveToY == self.y+1 else False
        self.isOccupied = occupied
        if self.isForward and not self.isOccupied:
            self.y = moveToY
            return False    #   don't take opp pawn
        elif self.isDiagonal and self.isOccupied:
            self.y = moveToY
            self.x = moveToX
            return True     #   take opp pawn

A = [Pawn(0, 0), Pawn(1, 0), Pawn(2, 0)]
B = [Pawn(0, 2), Pawn(1, 2), Pawn(2, 2)]

def drawgrid():
    t.color("white")
    t.width(6)
    t.penup()
    t.goto(-150, -450)
    t.pendown()
    t.goto(-150, 450)
    t.penup()
    t.goto(150, -450)
    t.pendown()
    t.goto(150, 450)
    t.penup()
    t.goto(-450, 150)
    t.pendown()
    t.goto(450, 150)
    t.penup()
    t.goto(-450, -150)
    t.pendown()
    t.goto(450, -150)

def redraw():
    t.clear()
    drawgrid()
    t.penup()
    for pawn in A:
        y = (pawn.y * 300 - 450) + 80
        x = (pawn.x * 300 - 450) + 150
        t.goto(x, y)
        t.begin_fill()
        if pawn.selected:
            t.color("purple")
        else:
            t.color("red")
        t.circle(80)
        t.end_fill()

    for pawn in B:
        y = (pawn.y * 300 - 450) + 80
        x = (pawn.x * 300 - 450) + 150
        t.goto(x, y)
        t.begin_fill()
        t.color("blue")
        t.circle(80)
        t.end_fill()

def clicked(x, y):
    global A, B
    x = int((x+450)/300)
    y = int((y+450)/300)
    isSelected = -1
    isOccupied = -1
    for i in range(len(B)):
        if B[i].x == x and B[i].y == y:
            isOccupied = i
    for i in range(len(A)):
        if A[i].selected:
            isSelected = i
    if isSelected != -1:    #    if there is one selected, try to move it
        takeOpp = A[isSelected].move(isOccupied != -1, x, y)
        if takeOpp:
            B.pop(isOccupied)
        for i in range(len(A)):
            A[i].selected = False
    else:                   #   if there is nothing selected, then select it
        for i in range(len(A)):
            if x == A[i].x and y == A[i].y:
                A[i].selected = True

    redraw()

def main():
    redraw()
    screen.listen()
    screen.onclick(clicked)

main()

turtle.done()
