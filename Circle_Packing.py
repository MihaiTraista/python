import math
import pygame
import random
import sys

pygame.init()
canvas = pygame.display.set_mode((800, 800))

clock = pygame.time.Clock()


def get_distance_between_two_points(p1, p2):
    #   the square root of the sum of the squares of the other two sides
    x1, y1 = p1
    x2, y2 = p2
    base = x2 - x1
    height = y2 - y1
    hypotenuse = math.sqrt(base ** 2 + height ** 2)
    return hypotenuse


class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def grow(self):
        if self.x + self.radius > 800 or \
                self.x - self.radius < 0 or \
                self.y + self.radius > 800 or \
                self.y - self.radius < 0:
            return
        else:
            self.radius += 2


circles = [Circle(400, 400, 1)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
            pygame.quit()
            sys.exit()

    # Clear the screen
    canvas.fill((0, 0, 0))

    circles.append(Circle(random.randint(0, 800), random.randint(0, 800), 1))
    for circle in circles:
        circle.grow()
        pygame.draw.circle(canvas, (255, 255, 255), (circle.x, circle.y), circle.radius, 1)

    # Update the display
    pygame.display.flip()
    clock.tick(60)
