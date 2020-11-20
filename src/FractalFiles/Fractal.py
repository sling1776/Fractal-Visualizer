class Fractal:
    """
    Is a parent class for the mandelbrot and julia classes. It uses the Config object
    to determine its minX, minY and maxX. It can calculate the color of a pixel and
    can calculate the needed complex numbers to get the color.
    """
    def __init__(self):
        """
        stores name and min/max data. Stores Gradient.
        """
        raise NotImplementedError("Concrete subclass of Fractal must implement __init__")

# TODO: Spencer This method might be better if it only returned an integer. Rename it to be iteration count
    # This can also go in Mandelbrot
    def calculateIterations(self, row, col):
        """
        calculates the iterations for a set pixel.
        """
        raise NotImplementedError("Concrete subclass of Fractal must implement calculateIterations() method")

    def calculateComplexNumber(self, row, col):
        """
        calculates the needed complex numbers for color calculations
        """
        raise NotImplementedError("Concrete subclass of Fractal must implement calculateComplexNumber() method")



