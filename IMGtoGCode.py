from PIL import Image

# TODO: take filename from command line
# TODO: take all values from user input

# CURRENT INPUT -> OUTPUT
# Engraves image that is the (pixels / 10) in millimeters

# convert to greyscale
img = Image.open('testmeg.png').convert("L")
#img.save("testout.png", quality=100)

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

# Set height to use for image output (in mm)
OUTPUT_HEIGHT = 50.0

# Set pixels per mm
PIX_PER_MM = 10.0

# Set start X
START_X = 65.0
# Set start Y
START_Y = 11.5
# Set start Z
START_Z = 25.0

# Set Cutting Rate
CUT_RATE = 300
# Set Travel Rate
TRAVEL_RATE = 3000

# Set max power
MAX_POWER = 200
# Set min power
MIN_POWER = 30
# Set percent power
PERCENT_POWER = 0.1

# Set minimum value to ignore (0 is white, 255 is black)
IGNORE_UNDER = 25

# TODO: convert img list to new list that matches OUTPUT_WIDTH * PIXELS_PER_MM
"""new_height = OUTPUT_HEIGHT * PIX_PER_MM
print("New height: " + str(new_height))

size_ratio: float = new_height / height
print("Size ratio: " + str(size_ratio))

# DELETE THIS LATER
size_ratio = 1.5

if size_ratio > 1:  # Enlargen input list
    make_new_every = int(1 / (size_ratio - 1))
    print(make_new_every)
    new_row_counter = 0
    new_list = []
    for row in img_list:
        new_row = []
        new_col_counter = 0
        for col in range(0, len(row)):
            if new_col_counter == make_new_every:
                pass
elif size_ratio < 1:  # Shrink input list
    skip_every = int(1 / (1 - size_ratio))
    print(skip_every)
    pass
else:  # Output same list as inputted.
    pass"""

# convert list to within power settings (0 is black, 255 is white)
# TODO: convert to be within bounds of max and min power
print("Image size: " + str(col) + "px wide, " + str(row) + "px tall.")

out_list = []
for row in img_list:
    out_row = []
    for col in row:
        out_row.append(255 - col)
    out_list.append(out_row)

# make gcode file for output
gcode_out = open("output.gcode", "w", encoding="UTF-8")

gcode_out.write("G90\n")  # Absolute positioning
gcode_out.write("G21\n")  # Metric units

curr_x = START_X
max_x = START_X + width  # TODO: make the width based on img list not image
curr_y = START_Y
max_y = START_Y + height  # TODO: make the height based on img list not image

# increment units (1 / 10px/mm -> .1mm increase on each pixel
inc_by = 1 / PIX_PER_MM

# Start lasering
out_list = reversed(out_list)
for row in out_list:
    # Turn on laser
    curr_x = START_X
    gcode_out.write("G1 F" + str(CUT_RATE) + "\n")  # Set cut rate
    for col in row:
        if col > IGNORE_UNDER:
            gcode_out.write("M106 " + str(int(col * PERCENT_POWER)) + "\n")  # Set laser to power level
        else:
            gcode_out.write("M107\n")
        gcode_out.write("G1 X" + str(format(curr_x, ".1f")) + "\n")  # Move
        curr_x += inc_by
    gcode_out.write("M107\n")  # Turn laser off to move to next row
    curr_y += inc_by
    gcode_out.write("G1 X" + str(START_X) + " Y" + str(format(curr_y, ".1f")) + " F" + str(TRAVEL_RATE) + "\n")

