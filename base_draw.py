from logging import error
from PIL import Image, ImageDraw
import math

def hexagon_generator(edge_length, offset):
  """Generator for coordinates in a hexagon."""
  x, y = offset
  for angle in range(0, 360, 60):
    x += math.cos(math.radians(angle)) * edge_length
    y += math.sin(math.radians(angle)) * edge_length
    yield x, y

class BaseDraw():

    rectangle_size = (60, 20)
    center_offset = 20

    bases_color = {
        "A": "red",
        "T": "orange",
        "C": "blue",
        "G": "purple"
    }

    def __init__(self, image: Image.Image):
        self.image = image
        self.draw = ImageDraw.Draw(image)
        self.width, self.height = image.size
        self.center = self.width / 2

    def draw_phis(self, current_position: int):
        r = 10
        self.draw.line(
            (
                (self.center - self.center_offset - 130, current_position - 10),
                (self.center - self.center_offset - 110, current_position)
            ),
            fill="black"
        )
        self.draw.ellipse(
            (
                (self.center - self.center_offset - 130 - r, current_position - 10 - r),
                (self.center - self.center_offset - 130 + r, current_position - 10 + r)
            ),
            fill="grey"
        )

    def draw_hex(self, current_position: int):
        hexagon = hexagon_generator(20, (
            (self.center - self.center_offset - 110, current_position)
        ))
        self.draw.polygon(list(hexagon), fill='black')
        self.draw.line(
            (
                (self.center - self.center_offset - 100, current_position + 20),
                (self.center - self.center_offset - 130, current_position + 40)
            ),
            fill="black"
        )

    def draw_base_rect(self, current_position: int, color: str):
        self.draw.rectangle(
            (
                (self.center - self.rectangle_size[0] - self.center_offset, current_position),
                (self.center - self.center_offset, current_position + self.rectangle_size[1])
            ),
            fill=color
        )

    def draw_base_A(self, current_position: int):
        self.draw.chord(
            (
                (self.center - self.center_offset - 10, current_position),
                (self.center - self.center_offset + 10, current_position + self.rectangle_size[1])
            ),
            start=-90,
            end=90,
            fill=self.bases_color["A"]
        )

    def draw_base_T(self, current_position: int):
        self.draw.arc(
            (
                (self.center - self.center_offset, current_position),
                (self.center - self.center_offset + 20, current_position + self.rectangle_size[1])
            ),
            start=90,
            end=-90,
            fill=self.bases_color["T"]
        )

    def draw_base_C(self, current_position: int):
        self.draw.polygon(
            (
                (self.center - self.center_offset, current_position),
                (self.center - self.center_offset + 10, current_position + self.rectangle_size[1] / 2),
                (self.center - self.center_offset, current_position + self.rectangle_size[1])
            ),
            fill=self.bases_color["C"]
        )

    def draw_base_G(self, current_position: int):
        self.draw.polygon(
            (
                (self.center - self.center_offset, current_position),
                (self.center - self.center_offset + 10, current_position),
                (self.center - self.center_offset, current_position + self.rectangle_size[1] / 2),
                (self.center - self.center_offset + 10, current_position + self.rectangle_size[1]),
                (self.center - self.center_offset, current_position + self.rectangle_size[1])
            ),
            fill=self.bases_color["G"]
        )


    def draw_base(self, base: str, current_position: int):
        if base in self.bases_color:
            self.draw.line(
                (
                    (self.center - self.center_offset - 100, current_position + 20),
                    (self.center - self.rectangle_size[0] - self.center_offset, current_position + self.rectangle_size[1]/2)
                ),
                fill="black"
            ),
            self.draw.line(
                (
                    (self.center - 10, current_position + self.rectangle_size[1]/2),
                    (self.center, current_position + self.rectangle_size[1]/2)
                ),
                fill="black"
            )
            self.draw_base_rect(current_position, self.bases_color[base])
            if base == "A":
                self.draw_base_A(current_position)
            elif base == "T":
                self.draw_base_T(current_position)
            elif base == "C":
                self.draw_base_C(current_position)
            elif base == "G":
                self.draw_base_G(current_position)
        else:
            error("Invalid base entered A T C G")

