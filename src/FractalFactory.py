from Julia import Julia
from Mandelbrot import Mandelbrot
from Mandelbrot3 import Mandelbrot3
import sys


class FractalFactory:
    def __init__(self):
        """
        """
        self.defaultDictionary = {'type': "mandelbrot",
                                  'pixels': 640,
                                  'centerx': 0.0,
                                  'centery': 0.0,
                                  'axislength': 4.0,
                                  'iterations': 78
                                  }

    def makeFractal(self, fractalFile=""):
        """
        This method will open the file given to it. if none is given, then it will make
        a default fractal. It uses the configuration file to make the fractal object.
        """
        if fractalFile != "":
            # this part we will open the file
            file = open(fractalFile)
            dic = self.extractFileContents(file)
            if dic['type'] == "mandelbrot":
                fractal = Mandelbrot(dic)
            elif dic['type'] == "julia":
                fractal = Julia(dic)
            elif dic['type'] == "mandelbrot3":
                fractal = Mandelbrot3(dic)
        else:
            fractal = Mandelbrot(self.defaultDictionary)

        return fractal

    def extractFileContents(self, file):
        dictionary = {}
        for line in file:
            if (not line.startswith("#")) and (": " in line):
                l = line.split(": ")
                key = l[0].lower()
                value = l[1].rstrip("\n").lower()
                if value.isdigit():
                    value = int(value)
                elif self.isFloat(value):
                    value = float(value)
                dictionary[key] = value
        return dictionary

    def isFloat(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False


if __name__ == '__main__':
    f = sys.argv[1]
    fracFac = FractalFactory()
    fracFac.makeFractal(f)
