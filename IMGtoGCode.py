from PIL import Image

# TODO: take filename from command line

# convert to greyscale
img = Image.open('test.jpg').convert("L")
img.save("testout.png", quality=100)

# Get size of image
width, height = img.size

# Create list of all pixel values in grey scale
# 3D array of rows, with each pixel in that row inside
img_list = []
for row in range(0, height-1):
    new_row = []
    for col in range(0, width-1):
        new_row.append(img.getpixel((col, row)))
    img_list.append(new_row)

# Set width to use for image output (in mm)
OUTPUT_WIDTH = 50.0

# Set pixels per mm
PIX_PER_MM = 10.0

# Set start X
START_X = 65.0
# Set start Y
START_Y = 11.5
# Set start Z
START_Z = 25.0

# Set Cutting Rate
CUT_RATE = 250
# Set Travel Rate
TRAVEL_RATE = 3000

# Set max power
MAX_POWER = 200
# Set min power
MIN_POWER = 30

# Set minimum value to ignore (0 is black, 255 is white)
IGNORE_OVER = 250

# TODO: convert img list to new list that matches OUTPUT_WIDTH * PIXELS_PER_MM

# TODO: convert list to within power settings (0 is black, 255 is white)

print(img_list[4])