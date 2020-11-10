from Fractal import Fractal
'''
This is the Julia Fractal. It is an extension of the Fractal Class. It has the unique information
and calculations needed for the specific fractals.
'''
class Julia(Fractal):
    def __init__(self, name, gradient, minX, maxX, minY):
        Fractal.__init__(self, name, gradient, minX, maxX, minY)
        self.c = complex(-1.0, 0.0)

    def calculateColor(self, row, col):
        self.resetZ()
        MAX_ITERATIONS = 78
        z = self.calculateComplexNumber(row, col)
        for i in range(MAX_ITERATIONS):
            z = z * z + self.c  # note: This is not the same as a mandelbrot z.
            if abs(z) > 2:
                return self.gradient.getColor(i)
        return self.gradient.getColor(MAX_ITERATIONS - 1)
