import random
import math
from PIL import Image, ImageColor

width = 901
height = 901
new_img = Image.new("RGBA", (width, height), "black")


def draw_jittery_line(exponent):
    x = 450
    y = 450

    offset = random.randint(0, 360)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(0, 128))
    # color = (255, 255, 255, random.randint(0, 128))

    for i in range(500):
        if x >= 900 or y >= 900 or x <= 0 or y <= 0:
            break
        color = (color[0], color[1], color[2], int((500 - i) / 500 * 255))
        # color = (color[0], color[1], color[2], 255)
        angle = random.random()
        angle = math.pow(angle, exponent)
        angle *= 360
        angle = (angle + offset) % 360
        x += 1 * math.cos(math.radians(angle))
        y += 1 * math.sin(math.radians(angle))
        new_img.putpixel((int(x), int(y)), color)


for i in range(1, 500):
    draw_jittery_line(math.pow(random.random(), 0.4))


new_img.save("/Users/mihaitraista/Desktop/new_image.png")
print("done!")


