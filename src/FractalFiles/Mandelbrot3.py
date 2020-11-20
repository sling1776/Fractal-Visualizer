from FractalFiles.Fractal import Fractal

"""
An Extension of the Fractal Class. Updates the z value and the resetZ function.
"""
class Mandelbrot3(Fractal):
    def __init__(self, dictionary):
        self.MAX_ITERATIONS = dictionary['iterations']
        cenX = dictionary['centerx']
        cenY = dictionary['centery']
        axisLen = dictionary['axislength']
        self.width = dictionary['pixels']
        self.height = dictionary['pixels']

        self.minX = cenX - (axisLen / 2.0)
        self.maxX = cenX + (axisLen / 2.0)
        self.minY = cenY - (axisLen / 2.0)

        self.z = complex(0, 0)
        self.c = complex(-1, 0)
        self.pixelSize = abs(self.maxX - self.minX) / self.width

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
        self.c = complex(x, y)

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height
