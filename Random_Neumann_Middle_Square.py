# generating a pseudo random number based on von Neumann's the "middle square" method
# https://en.wikipedia.org/wiki/Middle-square_method

# challenge 1 write a function that takes a seed and returns the middle squared
# challenge 2 calculate the period for any given seed for 8-digit numbers, 4-digit seed

#   https://www.youtube.com/watch?v=zWL3z7NMqAs&ab_channel=Socratica

import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.setup(height=900, width=900)
turtle.colormode(255)
t.shape("turtle")
t.width(3)
turtle.bgcolor(0, 40, 50)
t.speed(6)
t.color("orange")


def rotate(l, n):
    return l[n:] + l[:n]


def middleSquare(newSeed):
    squared = newSeed * newSeed
    l = [int(digit) for digit in str(squared)]
    for i in range(len(l), 8):
        l.append(0)
        if i % 2 == 0:
            l = rotate(l, -1)
#    print("squared = ", squared, "; l = ", l)
    l = l[2:]
    l = l[:4]
    string = ''.join(str(e) for e in l)
    return(int(string))


seed = 122
prev_seed = 0
counter = 0
scale = 50
t.penup()
t.goto(-200, -200)
t.pendown()

for i in range(100000):
    seed = middleSquare(seed)
    counter += seed
    if i % 50 == 0:
        print("i = ", i, "; seed = ", seed)
        t.clear()
    t.goto(t.xcor() + (seed-4500) / scale, t.ycor() + (prev_seed - 4500) / scale)
    prev_seed = seed

print("avg = ", counter / 100000)
turtle.mainloop()

