import colour
from GradientFiles.Gradient import Gradient
class StandGradient(Gradient):
    """
    This is the basic gradient. It is what we saw originally in the original program.
    """
    def __init__(self, number):
        self.startColor = colour.Color("#ffe4b5")
        self.endColor = colour.Color("#002277")
        self.colorList = list(self.startColor.range_to(self.endColor, number))

    def getColor(self, i):
        return self.colorList[i].get_hex_l()
