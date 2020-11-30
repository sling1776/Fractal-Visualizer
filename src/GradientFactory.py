from GradientFiles.Greyscale import Greyscale
from GradientFiles.StandGradient import StandGradient
from GradientFiles.RedToWhite import RedToWhite
from GradientFiles.BlueGreen import BlueGreen
from GradientFiles.threeColor import ThreeColor

class GradientFactory:
    def __init__(self):
        """

        """
        self.gradientList = ["standgradient", "redtowhite", "greyscale", "bluegreen", "threecolor"]

    def makeGradient(self, name, number):
        if name in self.gradientList:
            if name == self.gradientList[0]:
                return StandGradient(number)
            elif name == self.gradientList[1]:
                return RedToWhite(number)
            elif name == self.gradientList[2]:
                return Greyscale(number)
            elif name == self.gradientList[3]:
                return BlueGreen(number)
            elif name == self.gradientList[4]:
                return ThreeColor(number)
        elif name == "":
            return StandGradient(number)
        else:
            raise NotImplementedError("Given Gradient does not exist")
