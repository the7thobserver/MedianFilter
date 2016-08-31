#!/usr/bin/env python

from PIL import Image

def median(lst):
    even = (0 if len(lst) % 2 else 1) + 1
    half = (len(lst) - 1) / 2
    return sum(sorted(lst)[half:half + even]) / float(even)

images = []

# Load the images with the blocking object
for x in range(1, 10):
    print "Loading image #" + str(x)
    images.append(Image.open("pics/" + str(x) + ".png"))
    print "   ", images[x - 1].format, images[x - 1].size, images[x - 1].mode   

width, height = images[0].size
# The resulting image without the object
new_image = Image.new('RGB', (width, height))

r_buffer = []
g_buffer = []
b_buffer = []

print "Processing image..."

for x in range(0, width):
    for y in range(0, height):
        # Iterate over all the pictures and gather their rgb values
        for i in range(0, len(images)):
            r, g, b = images[i].getpixel((x,y))
            r_buffer.append(r)
            g_buffer.append(g)
            b_buffer.append(b)

        # Our median filter
        median_value = (int(median(r_buffer)), int(median(g_buffer)), int(median(b_buffer)))

        # Empty the buffers
        r_buffer[:] = []
        g_buffer[:] = []
        b_buffer[:] = []

        new_image.putpixel((x,y), median_value)
    print "Still working on it!"

new_image.save("result.png")

