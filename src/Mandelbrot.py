from Fractal import Fractal
"""
An Extension of the Fractal Class. Updates the z value and the resetZ function.
"""
class Mandelbrot(Fractal):
    def __init__(self, config, gradient, image):
        Fractal.__init__(self, config, gradient, image)
        self.z = complex(0, 0)

    def resetZ(self):
        self.z = complex(0, 0)
