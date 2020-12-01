import unittest
from GradientFiles.Gradient import Gradient
from oldFiles.Config import Config
from FractalFiles.Mandelbrot import Mandelbrot


# autocmd BufWritePost <buffer> !python3 runTests.py

class TestMandelbrot(unittest.TestCase):
    config = Config()
    gradient = Gradient()
    def test_colorOfThePixelMandelbrot(self):
        man = Mandelbrot(self.config, self.gradient, "mandelbrot")
        self.assertEqual(man.calculateColor(0, 0), "#ffe4b5")
        self.assertEqual(man.calculateColor(10, 10), "#ffe4b5")
        self.assertEqual(man.calculateColor(20, 20), "#ffe4b5")
        self.assertEqual(man.calculateColor(300, 300), "#002277")
        self.assertEqual(man.calculateColor(512, 512), "#ffe5b2")
        self.assertEqual(man.calculateColor(1000, 1000), "#ffe4b5")


    def test_colorOfThePixelSpiral0(self):
        man = Mandelbrot(self.config, self.gradient, "spiral0")
        self.assertEqual(man.calculateColor(0, 0), "#002277")
        self.assertEqual(man.calculateColor(10, 10), "#002277")
        self.assertEqual(man.calculateColor(20, 20), "#002277")
        self.assertEqual(man.calculateColor(300, 300), "#0073a2")
        self.assertEqual(man.calculateColor(512, 512), "#6cff40")
        self.assertEqual(man.calculateColor(1000, 1000), "#85ff4a")

    def test_colorOfThePixelSpiral1(self):
        man = Mandelbrot(self.config, self.gradient, "spiral1")
        self.assertEqual(man.calculateColor(0, 0), "#002277")
        self.assertEqual(man.calculateColor(10, 10), "#002277")
        self.assertEqual(man.calculateColor(20, 20), "#002277")
        self.assertEqual(man.calculateColor(300, 300), "#002277")
        self.assertEqual(man.calculateColor(512, 512), "#002277")
        self.assertEqual(man.calculateColor(1000, 1000), "#002277")

    def test_colorOfThePixelSeahorse(self):
        man = Mandelbrot(self.config, self.gradient, "seahorse")
        self.assertEqual(man.calculateColor(0, 0), "#85ff4a")
        self.assertEqual(man.calculateColor(10, 10), "#7dff47")
        self.assertEqual(man.calculateColor(20, 20), "#47ff33")
        self.assertEqual(man.calculateColor(300, 300), "#00de9e")
        self.assertEqual(man.calculateColor(512, 512), "#002277")
        self.assertEqual(man.calculateColor(1000, 1000), "#002277")

    def test_colorOfThePixelElephants(self):
        man = Mandelbrot(self.config, self.gradient, "elephants")
        self.assertEqual(man.calculateColor(0, 0), "#95ff51")
        self.assertEqual(man.calculateColor(10, 10), "#a4ff58")
        self.assertEqual(man.calculateColor(20, 20), "#b9ff62")
        self.assertEqual(man.calculateColor(300, 300), "#002277")
        self.assertEqual(man.calculateColor(512, 512), "#a4ff58")
        self.assertEqual(man.calculateColor(1000, 1000), "#00d4ab")

    def test_colorOfThePixelLeaf(self):
        man = Mandelbrot(self.config, self.gradient, "leaf")
        self.assertEqual(man.calculateColor(0, 0), "#ddff76")
        self.assertEqual(man.calculateColor(10, 10), "#ddff76")
        self.assertEqual(man.calculateColor(20, 20), "#ddff76")
        self.assertEqual(man.calculateColor(300, 300), "#b9ff62")
        self.assertEqual(man.calculateColor(512, 512), "#c6ff68")
        self.assertEqual(man.calculateColor(1000, 1000), "#bfff65")

    def test_getNameMandelbrot(self):
        man = Mandelbrot(self.config, self.gradient, "mandelbrot")
        self.assertEqual(man.getName(), "mandelbrot")


if __name__ == '__main__':
    unittest.main()
