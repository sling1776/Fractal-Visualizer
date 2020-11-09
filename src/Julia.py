from Fractal import Fractal

class Julia(Fractal):
    def __init__(self, name, gradient, minX, maxX, minY):
        Fractal.__init__(self, name, gradient, minX, maxX, minY)
        self.c = complex(-1.0, 0.0)

    def calculateColor(self, row, col):
        self.resetZ()
        MAX_ITERATIONS = 78
        z = self.calculateComplexNumber(row, col)
        for i in range(MAX_ITERATIONS):
            z = z * z + self.c  # Get z1, z2, ...
            if abs(z) > 2:
                return self.gradient.getColor(i)  # The sequence is unbounded
        return self.gradient.getColor(MAX_ITERATIONS - 1)  # Indicate a bounded sequence

    def resetZ(self):
        self.z = complex(-1.0, 0)
