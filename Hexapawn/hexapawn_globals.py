import turtle

COLUMNS = 3
ROWS = 3
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900
COLUMN_SIZE = SCREEN_WIDTH / COLUMNS
ROW_SIZE = SCREEN_HEIGHT / ROWS
SCREEN_TOP = SCREEN_HEIGHT/2
SCREEN_BOTTOM = (SCREEN_HEIGHT/2) * -1
SCREEN_LEFT = (SCREEN_WIDTH/2) * -1
SCREEN_RIGHT = SCREEN_WIDTH/2
SELECT_FLAG = 1000

player = [0, 1, 2]
computer = [0, 1, 2]
turn_number = 1

turtle.colormode(255)
screen = turtle.Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor(0, 0, 0)
t = turtle.Turtle()
t.speed(0)
t.penup()
t.shape("turtle")
#   t.hideturtle()
turtle.tracer(2)


def offset_coord(received_value):
    return received_value - SCREEN_HEIGHT / 2
