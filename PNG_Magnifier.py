# take a pixel art PNG of 32x32 and magnify it

from PIL import Image

input_image = Image.open("/Users/username/Desktop/3232.png")

# Create a new image 64x64. Size can be changed later
output_image = Image.new("RGB", (64, 64), "white")

input_pixel = input_image.getpixel((0, 0))
print(input_pixel)

