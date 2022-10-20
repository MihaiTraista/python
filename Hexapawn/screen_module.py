import turtle
from hexapawn_globals import *


def draw_line(t, startX, startY, length, angle):
    t.penup()
    t.goto(startX, startY)
    t.setheading(angle)
    t.pendown()
    t.forward(length)


def draw_grid():
    t.color("white")
    t.width(6)
    for i in range(1, ROWS):
        draw_line(t, offset_coord(0), offset_coord(COLUMN_SIZE * i), SCREEN_WIDTH, 0)
        draw_line(t, offset_coord(ROW_SIZE * i), offset_coord(0), SCREEN_WIDTH, 90)


def draw_pieces(player, computer):
    t.penup()
    for turn in range(2):
        pawnList = player if turn == 0 else computer
        for pawn in pawnList:
            selectedFlagValue = SELECT_FLAG if pawn >= SELECT_FLAG else 0
            pawn -= selectedFlagValue
            x = pawn % COLUMNS if turn == 0 else COLUMNS - 1 - pawn % COLUMNS               #   get x and y values between 0 and 2
            y = int(pawn / COLUMNS) if turn == 0 else (COLUMNS - 1 - int(pawn / COLUMNS))
            x = offset_coord(x * COLUMN_SIZE + COLUMN_SIZE * 0.8)                           #   scale and offset x and y values
            y = offset_coord(y * COLUMN_SIZE + ROW_SIZE * 0.5)
            t.goto(x, y)
            if selectedFlagValue:
                t.color("purple")
            elif turn == 0:
                t.color("red")
            else:
                t.color("blue")
            t.begin_fill()
            t.circle(COLUMN_SIZE * 0.3)
            t.end_fill()


def update(player, computer):
    t.clear()
    draw_grid()
    draw_pieces(player, computer)