import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screenHeight = 1000
screenWidth = 1000
screen.setup(height=screenHeight, width=screenWidth)
t.hideturtle()
turtle.colormode(255)
t.shape("turtle")
t.width(3)
t.speed(0)
t.color("green")
t.penup()
t.goto(-500, -450)

turtle.done()