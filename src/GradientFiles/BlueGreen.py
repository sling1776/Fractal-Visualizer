import colour
from GradientFiles.Gradient import Gradient
class BlueGreen(Gradient):
    """
    This is the blue green Gradient.
    """
    def __init__(self, number):
        self.startColor = colour.Color("blue")
        self.endColor = colour.Color("green")
        self.colorList = list(self.startColor.range_to(self.endColor, number))

    def getColor(self, i):
        return self.colorList[i].get_hex_l()