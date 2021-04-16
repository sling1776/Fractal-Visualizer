from FractalFiles.Fractal import Fractal
from FractalFiles.Julia import Julia

'''
This is the Julia Fractal. It is an extension of the Fractal Class. It has the unique information
and calculations needed for the specific fractals.
'''
class Julia3(Julia):
    def __init__(self, dictionary):
        super().__init__(dictionary)

    def calculateIterations(self, row, col):
        """
        calculates the iterations for a set pixel.
        """
        self.calculateComplexNumber(row, col)
        z = self.z
        c = self.c
        for i in range(self.MAX_ITERATIONS):
            z = z * z * z + c
            if abs(z) > 2:
                return i
        return self.MAX_ITERATIONS - 1

    def calculateComplexNumber(self, row, col):
        """
        @Override
        calculates the needed complex numbers for color calculations
        """
        x = self.minX + col * self.pixelSize
        y = self.minY + (self.width-row) * self.pixelSize
        self.z = complex(x, y)

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height
