import math

import colour
from GradientFiles.Gradient import Gradient
class ThreeColor(Gradient):
    """
    This is the greyscale Gradient.
    """
    def __init__(self, number):
        self.startColor = colour.Color("Red")
        self.middleColor = colour.Color("Blue")
        self.endColor = colour.Color("purple")
        iterationNumber = math.ceil((math.log2(number)))
        colorList1 = list(self.startColor.range_to(self.middleColor, iterationNumber))
        self.cList = []
        for i in range(len(colorList1)):
            colorList2 = list(colorList1[i].range_to(self.endColor, math.ceil(number / iterationNumber)))
            for item in colorList2:
                self.cList.append(item)

    def getColor(self, i):
        return self.cList[i].get_hex_l()
