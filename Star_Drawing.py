import turtle

# define turtle object
turtle.colormode(255)
tommy = turtle.Turtle()
screen = turtle.Screen()
tommy.shape("turtle")
tommy.speed(0)

# prepare for drawing
tommy.penup()
tommy.color("orange")
screen.bgcolor(0, 40, 50)


def draw_star(size, fillFlag):
    if fillFlag:
        tommy.begin_fill()
    else:
        tommy.pendown()
    for i in range(5):
        tommy.forward(size)
        tommy.right(144)
    if fillFlag:
        tommy.end_fill()
    else:
        tommy.penup()


tommy.goto(-100, 50)
for i in range(5):
    tommy.pendown()
    tommy.forward(200)
    for ii in range(5):
        tommy.forward(50)
        draw_star(20, True)
        tommy.right(144)
        tommy.right(144)
        tommy.penup()


