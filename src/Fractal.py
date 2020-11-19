from Gradient import Gradient

class Fractal:
    """
    Is a parent class for the mandelbrot and julia classes. It uses the Config object
    to determine its minX, minY and maxX. It can calculate the color of a pixel and
    can calculate the needed complex numbers to get the color.
    """
    def __init__(self, image, cenX, cenY, axisLen, height, width):
        """
        stores name and min/max data. Stores Gradient.
        """
        self.name = image
        self.MAX_ITERATIONS = Gradient().getLength()
        self.minX = cenX - (axisLen / 2.0)
        self.maxX = cenX + (axisLen / 2.0)
        self.minY = cenY - (axisLen / 2.0)
        self.height = height
        self.width = width
        self.z = complex(0, 0)
        self.c = complex(-1, 0)
        self.pixelSize = abs(self.maxX - self.minX) / 512

# TODO: Spencer This method might be better if it only returned an integer. Rename it to be iteration count
    # This can also go in Mandelbrot
    def calculateIterations(self, row, col):
        """
        calculates the iterations for a set pixel.
        """
        self.calculateComplexNumber(row, col)
        z = self.z
        c = self.c
        for i in range(self.MAX_ITERATIONS):
            z = z * z + c
            if abs(z) > 2:
                return i
        return self.MAX_ITERATIONS - 1

    def calculateComplexNumber(self, row, col):
        """
        calculates the needed complex numbers for color calculations
        """
        x = self.minX + col * self.pixelSize
        y = self.minY + (self.width-row) * self.pixelSize
        self.z = complex(x, y)

    def getName(self):
        return self.name


