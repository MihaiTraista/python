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

A = [0, 1, 2]
B = [0, 1, 3]

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
        selected = False
        if pawn >= 10:
            pawn -= 10
            selected = True
        y = (int(pawn/3) * 300 - 450) + 80
        x = ((pawn%3) * 300 - 450) + 150
        t.goto(x, y)
        t.begin_fill()
        if selected:
            t.color("purple")
        else:
            t.color("red")
        t.circle(80)
        t.end_fill()

    for pawn in B:
        y = ((2-int(pawn/3)) * 300 - 450) + 80
        x = ((2-(pawn%3)) * 300 - 450) + 150
        t.goto(x, y)
        t.begin_fill()
        t.color("blue")
        t.circle(80)
        t.end_fill()

def computerTurn():


def clicked(x, y):
    global A, B

    column = int((x+450)/300)
    row = int((y+450)/300)
    square = column + (row*3)
    pawnToMove = -1

    #   select pawn
    for i in range(len(A)):
        if A[i] >= 10:
            A[i] -= 10
            pawnToMove = i
        if A[i] == square:
            A[i] += 10
    if max(A) >= 10:
        pawnToMove = -1

    print("A before move ", A, " pawnToMove: ", pawnToMove, " square: ", square)
    if pawnToMove != -1:
        prev = A[pawnToMove]
        moveTryForward = True if square % 3 == prev % 3 else False
        moveTryOneSquare = True if square > prev and square - prev <= 4 else False
        moveTryFree = False if 8-square in B else True
        moveTryEndOfBoard = True if square >= 6 else False
        #   moveTryCheckmate = True if

        #   is it ONE square or JUMP
        #   is it FORWARD or DIAGONALLY?
        #   is the new pawn FREE?
        #   WIN_1 did it reach the end of the board?
        #   WIN_2 does the other player have moves?
        #   WIN_3 eliminated all your opponents pieces?

        if moveTryForward and moveTryOneSquare and moveTryFree:
            A[pawnToMove] = square
        elif not moveTryForward and moveTryOneSquare and not moveTryFree:
            A[pawnToMove] = square
            B.remove(8-square)
        if max(A) > 5 or sum(B) == -3:
            redraw()
            t.penup()
            t.goto(0, -300)
            t.color('white')
            t.write("You won!", move=False, align="center", font=("Arial", 50, "bold"))
            return

        print(moveTryForward, moveTryOneSquare, moveTryFree, moveTryEndOfBoard)
        print("After move, ready for Computer turn: ", A, B)

        computerTurn()

    #   A can move one square forward if the square is free
    #   A can move diagonally if B is there. A eats B
    #   A player loses if they have no legal moves or the other player reaches the end of the board with a pawn.

    redraw()

def main():
    redraw()
    screen.listen()
    screen.onclick(clicked)

main()

turtle.done()
