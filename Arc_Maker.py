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


def get_angle_of_line(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    adjacent = x2 - x1
    opposite = y2 - y1
    if adjacent == 0 and opposite > 0:
        #   Line points upwards
        angle = 0
    elif adjacent == 0 and opposite < 0:
        #   Line points downwards
        angle = math.pi
    elif opposite == 0 and adjacent > 0:
        #   Line points to the right
        angle = math.pi / 2
    elif opposite == 0 and adjacent < 0:
        #   Line points to the left
        angle = 3 * (math.pi / 2)
    else:
        angle = math.atan(opposite / adjacent)
        if adjacent < 0:
            angle += math.pi
        angle = math.pi / 2 - angle

    #   print(f"p1 {p1} p2 {p2} opposite {opposite}, adjacent {adjacent}, angle {math.degrees(angle)}")
    return angle

