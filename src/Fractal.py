class Fractal:
    """
    Is a parent class for the mandlebrot and julia classes. It uses the Config object
    to determine its minX, minY and maxX. It can calculate the color of a pixel and
    can calculate the needed complex numbers to get the color.
    """
    def __init__(self, config, gradient, image):
        """
        stores name and min/max data. Stores Gradient.
        """
        fracType = config.getFractal(image)
        # get configuration data from dictionary
        cenX = config.getImageInformation('centerX', fracType, image)
        cenY = config.getImageInformation('centerY', fracType, image)
        axislen = config.getImageInformation('axisLen', fracType, image)

        self.name = image
        self.gradient = gradient
        self.minX = cenX - (axislen / 2.0)
        self.maxX = cenX + (axislen / 2.0)
        self.minY = cenY - (axislen / 2.0)
        self.z = complex(0, 0)
        self.pixelSize = abs(self.maxX - self.minX) / 512

    def calculateColor(self, row, col):
        """
        calculates the color of a given pixel
        """
        """Return the color of the current pixel within the Mandelbrot set"""
        self.resetZ()
        MAX_ITERATIONS = self.gradient.getLength()
        for i in range(MAX_ITERATIONS):
            self.z = self.z * self.z + self.calculateComplexNumber(row, col)
            if abs(self.z) > 2:
                return self.gradient.getColor(i)
        return self.gradient.getColor(MAX_ITERATIONS - 1)

    def calculateComplexNumber(self, row, col):
        """
        calculates the needed complex numbers for color calculations
        """
        x = self.minX + col * self.pixelSize
        y = self.minY + row * self.pixelSize
        return complex(x, y)

    def getName(self):
        return self.name

    def resetZ(self):
        self.z = complex(0, 0)


