from PIL import Image, ImageDraw
import math
img = Image.new('RGBA', (960, 960), (255, 255, 255))
draw = ImageDraw.Draw(img)
kyt = math.radians(60)
with open("DS5.txt", "r") as file:
    for line in file:
        coords_list = line.split()
        i = int(coords_list[0]) - 480
        j = int(coords_list[1]) - 480
        x = math.cos(kyt) * i - math.sin(kyt) * j
        y = math.sin(kyt) * i + math.cos(kyt) * j
        draw.line((x + 480, y + 480, x + 481, y + 481), fill=(0, 190, 255))
img.show()
img.save('result.png')
