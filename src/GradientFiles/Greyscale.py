import colour
from GradientFiles.Gradient import Gradient
class Greyscale(Gradient):
    """
    This is the greyscale Gradient.
    """
    def __init__(self, number):
        self.startColor = colour.Color("white")
        self.endColor = colour.Color("black")
        self.colorList = list(self.startColor.range_to(self.endColor, number))

    def getColor(self, i):
        return self.colorList[i].get_hex_l()
