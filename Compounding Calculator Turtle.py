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
results = []


def rect(x, y, width, height, year, value):
    t.goto(x, y)
    t.begin_fill()
    t.setheading(0)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.sety(t.ycor()+10)
    t.write("£"+str(int(value)), font=("Arial", 10, "bold"))
    t.sety(t.ycor()-20)
    t.left(90)
    t.forward(height)
    t.end_fill()
    t.sety(t.ycor()-20)
    t.write(year, font=("Arial", 16, "bold"))


def plot(columns):
    columnWidth = screenWidth / (columns + 4) - 100 / (columns + 4)
    for i in range(columns):
        newHeight = results[i] * ((screenHeight-80) / max(results))
        rect(t.xcor() + columnWidth + columnWidth / 10, -450, columnWidth, newHeight, i + 1, results[i])


def main():
    principal = screen.numinput("Rich indeed", "Enter principal: ", None, minval=10, maxval=100000)
    rate = screen.numinput("Rich indeed", "Annual Rate: ", None, minval=-1000, maxval=1000)
    years = int(screen.numinput("Rich indeed", "Years: ", None, minval=1, maxval=100))
    for year in range(years):
        principal = principal * (1 + rate/100)
        results.append(principal)
    plot(years)


main()
turtle.done()