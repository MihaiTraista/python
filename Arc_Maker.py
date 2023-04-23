from turtle import *
import math

shape("turtle")
bgcolor("black")
color("red")
dot(5)
color("orange")
width(4)
speed(0)
#tracer(10)


def get_distance_between_two_points(p1, p2):
    #   the square root of the sum of the squares of the other two sides
    x1, y1 = p1
    x2, y2 = p2
    base = x2 - x1
    height = y2 - y1
    hypotenuse = math.sqrt(base ** 2 + height ** 2)
    return hypotenuse

