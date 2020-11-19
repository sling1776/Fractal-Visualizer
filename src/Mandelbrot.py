from Fractal import Fractal
"""
An Extension of the Fractal Class. Updates the z value and the resetZ function.
"""
class Mandelbrot(Fractal):
    def __init__(self, image, cenX, cenY, axisLen, height, width):
        Fractal.__init__(self, image, cenX, cenY, axisLen, height, width)
        self.z = complex(0, 0)

    def calculateComplexNumber(self, row, col):
        """
        @Override
        calculates the needed complex numbers for color calculations
        """
        x = self.minX + col * self.pixelSize
        y = self.minY + (self.width-row) * self.pixelSize
        self.c = complex(x, y)