# take a pixel art PNG of 32x32 and magnify it

from PIL import Image

input_image = Image.open("/Users/username/Desktop/3232.png")

# Create a new image 64x64. Size can be changed later
output_image = Image.new("RGB", (64, 64), "white")

input_pixel = input_image.getpixel((0, 0))
print(input_pixel)


def stretch_wide():
    for x in range(64):
        for y in range(64):
            input_coord = (x // 4 + 9, y // 2)
            color = input_image.getpixel(input_coord)
            # print(color)
            output_coord = (x, y)
            output_image.putpixel(output_coord, color)


stretch_wide()
# magnify(20)
output_image.save("/Users/mihaitraista/Desktop/6464.png")
