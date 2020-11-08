from Fractal import Fractal

class Julia(Fractal):
    def __init__(self, name, gradient, minX, maxX, minY):
        Fractal.__init__(self, name, gradient, minX, maxX, minY)
        self.z = complex(-1.0, 0.0)

    def resetZ(self):
        self.z = complex(-1.0, 0)
