import turtle

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
B = [0, 1, 2]

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
        if pawn > 2:
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

def playermove(square):
    for i in range(len(A)):
        if A[i] == square:
            print("You can't move here")
            return
    for i in range(len(B)):
        if B[i] == square:
            if (square % 3) == B[i]:
                print("You can't move here")
                return
            else:
                print("b lost a pawn")
                B[i] = -1

def clicked(x, y):
    global A, B

    column = int((x+450)/300)
    row = int((y+450)/300)
    square = column + (row*3)

    #   select pawn
    if (max(A) < 10 and max(A) != square+10) or (max(A) >= 10 and any(a == square for a in A)):
        for i in range(len(A)):
            if A[i] == square:
                A[i] += 10
            elif A[i] >= 10:
                A[i] -= 10
    #   elif max(A) == square + 10:
        #   do nothings
    #   select another

    print("A = ", A)

#    playermove(square)
    redraw()

def main():
    redraw()
    screen.listen()
    screen.onclick(clicked)

main()

turtle.done()
