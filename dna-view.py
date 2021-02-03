from logging import error
from PIL import Image, ImageDraw
import sys

args = sys.argv

nito_bases = {
    "A": "T",
    "T": "A",
    "C": "G",
    "G": "C"
}

bases_color = {
    "A": "red",
    "T": "yellow",
    "C": "blue",
    "G": "purple"
}

bases = args[1].upper()

height = len(bases) * 50 + 100
width = 300

center = width/2
center_offset = 20

current_index = 1

rectangle_size = (60, 20)

image = Image.new("RGB", (width, height), color="white")
draw = ImageDraw.Draw(image)

for base in bases:
    if base not in nito_bases:
        error("Enter a valid base sequence " + " ".join(nito_bases.keys()))

    current_position = current_index * 50

    draw.rectangle(
        (

            (center - rectangle_size[0] - center_offset, current_position),
            (center - center_offset, current_position + rectangle_size[1])
        ),
        fill="black"
    )

    # OTHER STAND

    draw.rectangle(
        (

            (center + rectangle_size[0] + center_offset, current_position),
            (center + center_offset, current_position + rectangle_size[1])
        ),
        fill="black"
    )

    current_index += 1

image.save("dna-view.png")

