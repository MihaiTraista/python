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




for i in range(1, 500):
    draw_jittery_line(math.pow(random.random(), 0.4))


new_img.save("/Users/mihaitraista/Desktop/new_image.png")
print("done!")


