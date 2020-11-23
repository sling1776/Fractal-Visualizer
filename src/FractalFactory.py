from FractalFiles.Julia import Julia
from FractalFiles.Mandelbrot import Mandelbrot
from FractalFiles.Mandelbrot3 import Mandelbrot3
from FractalFiles.Mandelbrot4 import Mandelbrot4
from FractalFiles.BurningShip import BurningShip
from FractalFiles.Julia3 import Julia3
from FractalFiles.BurningShipJulia import BurningShipJulia
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
                                  'iterations': 100
                                  }

    def makeFractal(self, fractalFile=""):
        """
        This method will open the file given to it. if none is given, then it will make
        a default fractal. It uses the configuration file to make the fractal object.
        """
        if fractalFile != "":
            file = open(fractalFile)
            dic = self.extractFileContents(file)
            if dic['type'] == "mandelbrot":
                fractal = Mandelbrot(dic)
            elif dic['type'] == "julia":
                fractal = Julia(dic)
            elif dic['type'] == "mandelbrot3":
                fractal = Mandelbrot3(dic)
            elif dic['type'] == "mandelbrot4":
                fractal = Mandelbrot4(dic)
            elif dic['type'] == "burningshipjulia":
                fractal = BurningShipJulia(dic)
            elif dic['type'] == "julia3":
                fractal = Julia3(dic)
            elif dic['type'] == "burningship":
                fractal = BurningShip(dic)
        else:
            fractal = Mandelbrot(self.defaultDictionary)

        return fractal

    def extractFileContents(self, file):
        dictionary = {}
        for line in file:
            if (not line.startswith("#")) and (": " in line):
                l = line.split(": ")
                key = l[0].lower()
                value = l[1].rstrip("\n").strip().lower()
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
