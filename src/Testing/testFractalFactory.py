import unittest
from FractalFactory import FractalFactory
from FractalFiles import Fractal, BurningShipJulia, BurningShip, Julia3, Julia, Mandelbrot4, Mandelbrot, Mandelbrot3
import os


class TestFractalFactory(unittest.TestCase):
    fac = FractalFactory()
    dic = {
        'type': "mandelbrot",
        'pixels': 640,
        'iterations': 100,
        'centerx': 0.354996007077539,
        'centery': -0.33864748057364,
        'axislength': 0.000149685953411638
    }
    cwd = os.getcwd()
    if "lingwall-spencer-assn4" in cwd:
        if not cwd.endswith("lingwall-spencer-assn4"):
            while not cwd.endswith("lingwall-spencer-assn4"):
                os.chdir("..")
        f1 = open("data/branches100.frac")

    def test_makeFractal(self):
        myList = ["branches100.frac", "fulljulia.frac", "mandelthree.frac", "mandelfour.frac", "burningshipjulia.frac", "julia3.frac", "burningship.frac"]
        myList2 = [Mandelbrot.Mandelbrot, Julia.Julia, Mandelbrot3.Mandelbrot3, Mandelbrot4.Mandelbrot4, BurningShipJulia.BurningShipJulia, Julia3.Julia3, BurningShip.BurningShip]
        for i in range(len(myList)):
            self.dic['type'] = myList[i]
            self.assertIsInstance(self.fac.makeFractal("data/" + myList[i]), myList2[i])


    def test_extractFileContents(self):
            newDictionary = self.fac.extractFileContents(self.f1)
            self.assertEqual(newDictionary['type'], "mandelbrot")
            self.assertEqual(newDictionary['centerx'], 0.354996007077539)
            self.assertEqual(newDictionary['centery'], -0.33864748057364)
            self.assertEqual(newDictionary['pixels'], 640)
            self.assertEqual(newDictionary['iterations'], 100)
            self.assertEqual(newDictionary['axislength'], .000149685953411638)




if __name__ == '__main__':
    unittest.main()