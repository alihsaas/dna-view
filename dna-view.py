from logging import error
from PIL import Image
from base_draw import BaseDraw
import sys

args = sys.argv

nito_bases = {
    "A": "T",
    "T": "A",
    "C": "G",
    "G": "C"
}

bases = args[1].upper()

height = len(bases) * 50 + 100
width = 300

center = width/2

current_index = 1

main_image = Image.new("RGB", (width, height), color="white")

first_strand = Image.new("RGBA", (width, height), (0, 0, 0, 0))
second_strand = Image.new("RGBA", (width, height), (0, 0, 0, 0))

first_draw_strand = BaseDraw(first_strand)
second_draw_strand = BaseDraw(second_strand)

for base in bases:

    if base not in nito_bases:
        error("Enter a valid base sequence " + " ".join(nito_bases.keys()))

    current_position = current_index * 50

    first_draw_strand.draw_base(base, current_position)

    comp_base = nito_bases[base]

    second_draw_strand.draw_base(comp_base, current_position)

    current_index += 1

second_strand = second_strand.transpose(Image.FLIP_LEFT_RIGHT)

main_image.paste(first_strand, (0, 0), first_strand)
main_image.paste(second_strand, (0, 0), second_strand)

main_image.save("dna-view.png")
