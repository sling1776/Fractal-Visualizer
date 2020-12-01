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
        cList1 = list(self.startColor.range_to(self.middleColor, iterationNumber))
        self.colorList = []
        for i in range(len(cList1)):
            cList2 = list(cList1[i].range_to(self.endColor, math.ceil(number / iterationNumber)))
            for item in cList2:
                self.colorList.append(item)

    def getColor(self, i):
        return self.colorList[i].get_hex_l()
