from PIL import Image, ImageDraw
import math
img = Image.new('RGBA', (960, 960), (255, 255, 255))
draw = ImageDraw.Draw(img)
angle = math.radians(60)
with open("DS5.txt", "r") as file:
    for line in file:
        coords_list = line.split()
        i = int(coords_list[0]) - 480
        j = int(coords_list[1]) - 480
        x = math.cos(angle) * i - math.sin(angle) * j
        y = math.sin(angle) * i + math.cos(angle) * j
        draw.line((x + 480, y + 480, x + 481, y + 481), fill=(0, 190, 255))
img.show()
img.save('result.png')
