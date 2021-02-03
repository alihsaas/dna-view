from logging import error
from PIL import Image, ImageDraw

class BaseDraw():

    rectangle_size = (60, 20)
    center_offset = 20

    bases_color = {
        "A": "red",
        "T": "yellow",
        "C": "blue",
        "G": "purple"
    }

    def __init__(self, image: Image.Image):
        self.image = image
        self.draw = ImageDraw.Draw(image)
        self.width, self.height = image.size
        self.center = self.width / 2

    def draw_base_rect(self, current_position: int, color: str):
        self.draw.rectangle(
            (
                (self.center - self.rectangle_size[0] - self.center_offset, current_position),
                (self.center - self.center_offset, current_position + self.rectangle_size[1])
            ),
            fill=color
        )


    def draw_base_A(self, current_position: int):
        print("No Imp")

    def draw_base(self, base: str, current_position: int):
        if base in self.bases_color:
            self.draw_base_rect(current_position, self.bases_color[base])
            if base == "A":
                self.draw_base_A(current_position)
            elif base == "T":
                print("No Imp")
            elif base == "C":
                print("No Imp")
            elif base == "G":
                print("No Imp")
        else:
            error("Invalid base entered A T C G")

