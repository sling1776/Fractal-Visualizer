import colour
from GradientFiles.Gradient import Gradient
class RedToWhite(Gradient):
    """
    This is a red to white gradient.
    """
    def __init__(self, number):
        self.startColor = colour.Color("#620000")
        self.endColor = colour.Color("#ffffff")
        self.colorList = list(self.startColor.range_to(self.endColor, number))

    def getColor(self, i):
        return self.colorList[i].get_hex_l()