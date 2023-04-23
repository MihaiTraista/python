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


def arc(p1, p2, c):
    radius = get_distance_between_two_points(p1, c)
    angle_start = get_angle_of_line(c, p1)
    angle_end = get_angle_of_line(c, p2)
    span = angle_end - angle_start
    # print(f"angle_start {math.degrees(angle_start)}, "
    #       f"angle_end {math.degrees(angle_end)}, "
    #       f"span {math.degrees(span)}, "
    #       f"radius {radius}")
    penup()
    # print("x, y ", math.sin(angle_start) * radius + c[0], math.cos(angle_start) * radius + c[1])
    goto(math.sin(angle_start) * radius + c[0], math.cos(angle_start) * radius + c[1])
    dot(10)
    pendown()

    steps = int(radius / 4)
    if steps < 10:
        steps = 10
    for k in range(steps):
        angle = angle_start + (span / steps) * (k+1)
        x = math.sin(angle) * radius + c[0]
        y = math.cos(angle) * radius + c[1]
        goto(x, y)


for i in range(10):
    p1 = [0, 200]
    p2 = [0, -200]
    c = [i * 10, 0]
    arc(p1, p2, c)


done()
