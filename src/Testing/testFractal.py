import unittest
from FractalFiles import Fractal, BurningShipJulia, BurningShip, Julia3, Julia, Mandelbrot4, Mandelbrot, Mandelbrot3


class TestFractal(unittest.TestCase):
    dic = {
        'type': "mandelbrot",
        'pixels': 640,
        'iterations': 100,
        'centerx': 0.354996007077539,
        'centery': -0.33864748057364,
        'axislength': 0.000149685953411638
    }
    mand = Mandelbrot.Mandelbrot(dic)
    mand3 = Mandelbrot3.Mandelbrot3(dic)
    mand4 = Mandelbrot4.Mandelbrot4(dic)
    burnShip = BurningShip.BurningShip(dic)
    burnShipJ = BurningShipJulia.BurningShipJulia(dic)
    jul = Julia.Julia(dic)
    jul3 = Julia3.Julia3(dic)

    def test_calculateIterationsMand(self):
        self.assertEqual(self.mand.calculateIterations(0, 0), 75)
        self.assertEqual(self.mand.calculateIterations(50, 50), 75)
        self.assertEqual(self.mand.calculateIterations(100, 100), 76)

    def test_calculateIterationsMand3(self):
        self.assertEqual(self.mand3.calculateIterations(0, 0), 99)
        self.assertEqual(self.mand3.calculateIterations(50, 50), 99)
        self.assertEqual(self.mand3.calculateIterations(100, 100), 99)

    def test_calculateIterationsMand4(self):
        self.assertEqual(self.mand4.calculateIterations(0, 0), 99)
        self.assertEqual(self.mand4.calculateIterations(50, 50), 99)
        self.assertEqual(self.mand4.calculateIterations(100, 100), 99)

    def test_calculateIterationsBurnShip(self):
        self.assertEqual(self.burnShip.calculateIterations(0, 0), 4)
        self.assertEqual(self.burnShip.calculateIterations(50, 50), 4)
        self.assertEqual(self.burnShip.calculateIterations(100, 100), 4)

    def test_calculateIterationsBurnShipJulia(self):
        self.assertEqual(self.burnShipJ.calculateIterations(0, 0), 1)
        self.assertEqual(self.burnShipJ.calculateIterations(50, 50), 1)
        self.assertEqual(self.burnShipJ.calculateIterations(100, 100), 1)

    def test_calculateIterationsJul(self):
        self.assertEqual(self.jul.calculateIterations(0, 0), 99)
        self.assertEqual(self.jul.calculateIterations(50, 50), 99)
        self.assertEqual(self.jul.calculateIterations(100, 100), 99)

    def test_calculateIterationsJul3(self):
        self.assertEqual(self.jul3.calculateIterations(0, 0), 1)
        self.assertEqual(self.jul3.calculateIterations(50, 50), 1)
        self.assertEqual(self.jul3.calculateIterations(100, 100), 1)



if __name__ == '__main__':
    unittest.main()