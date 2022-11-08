import turtle
import math
import random

# define turtle object
t = turtle.Turtle()
screen = turtle.Screen()
screen.setup(900, 900)
t.shape("turtle")
t.speed(0)

# prepare for drawing
t.color("orange")
turtle.colormode(255)
screen.bgcolor(15, 15, 15)
turtle.tracer(19)
t.penup()
t.goto(-50, -100)
t.pendown()

currentColor = [128, 128, 128]


def slight_rand_color(amount, greyFlag):
    if greyFlag:
        currentColor[0] = (currentColor[0] + random.randint(amount*-1, amount)) % 256
        currentColor[1] = currentColor[0]
        currentColor[2] = currentColor[0]
    else:
        currentColor[0] = (currentColor[0] + random.randint(amount*-1, amount)) % 256
        currentColor[1] = (currentColor[1] + random.randint(amount*-1, amount)) % 256
        currentColor[2] = (currentColor[2] + random.randint(amount*-1, amount)) % 256
    t.color(currentColor[0], currentColor[1], currentColor[2])

def draw_recursive_hexagon(levels):
    if levels == 1:
        return
    else:
        size = (levels - 2) / 2
        size = math.pow(size, 0.2) * 70 + 5
        sides = 11-levels
        #   print(f'levels = {levels}, math.pow(size, 0.3) = {math.pow(((levels - 2) / 2), 0.3)} size = {size},\t\t\t sides = {sides}')
        for i in range(sides):
            slight_rand_color(2, True)
            t.forward(size)
            draw_recursive_hexagon(levels-1)
            t.left(360 / sides)


def main():
    draw_recursive_hexagon(6)

main()

turtle.done()