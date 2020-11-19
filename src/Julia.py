from Fractal import Fractal
'''
This is the Julia Fractal. It is an extension of the Fractal Class. It has the unique information
and calculations needed for the specific fractals.
'''
class Julia(Fractal):
    def __init__(self, image, cenX, cenY, axisLen, height, width):
        Fractal.__init__(self, image, cenX, cenY, axisLen, height, width)
        self.c = complex(-1.0, 0.0)

    def calculateComplexNumber(self, row, col):
        """
        @Override
        calculates the needed complex numbers for color calculations
        """
        x = self.minX + col * self.pixelSize
        y = self.minY + (self.width-row) * self.pixelSize
        self.z = complex(x, y)
