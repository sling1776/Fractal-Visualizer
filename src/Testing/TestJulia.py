import unittest
from FractalFiles.Julia import Julia
from GradientFiles.Gradient import Gradient
from oldFiles.Config import Config


# autocmd BufWritePost <buffer> !python3 runTests.py

class TestJulia(unittest.TestCase):
    config = Config()
    grad = Gradient()
    def test_colorOfThePixelFulljulia(self):
        man = Julia(self.config, self.grad, "fulljulia")
        self.assertEqual(man.calculateColor(0, 0), "#ffe4b5")
        self.assertEqual(man.calculateColor(10, 10), "#ffe4b5")
        self.assertEqual(man.calculateColor(20, 20), "#ffe4b5")
        self.assertEqual(man.calculateColor(300, 300), "#009cb3")
        self.assertEqual(man.calculateColor(512, 512), "#ffe4b5")
        self.assertEqual(man.calculateColor(1000, 1000), "#ffe4b5")

    def test_colorOfThePixelHourglass(self):
        man = Julia(self.config, self.grad, "hourglass")
        self.assertEqual(man.calculateColor(0, 0), "#009cb3")
        self.assertEqual(man.calculateColor(10, 10), "#009cb3")
        self.assertEqual(man.calculateColor(20, 20), "#009cb3")
        self.assertEqual(man.calculateColor(300, 300), "#009cb3")
        self.assertEqual(man.calculateColor(512, 512), "#009cb3")
        self.assertEqual(man.calculateColor(1000, 1000), "#009cb3")

    def test_colorOfThePixelLakes(self):
        man = Julia(self.config, self.grad, "lakes")
        self.assertEqual(man.calculateColor(0, 0), "#ffefa1")
        self.assertEqual(man.calculateColor(10, 10), "#ffefa1")
        self.assertEqual(man.calculateColor(20, 20), "#ffefa1")
        self.assertEqual(man.calculateColor(300, 300), "#fff797")
        self.assertEqual(man.calculateColor(512, 512), "#ffeaa8")
        self.assertEqual(man.calculateColor(1000, 1000), "#ffefa1")

    def test_getNameJulia(self):
        man = Julia(self.config, self.grad, "fulljulia")
        self.assertEqual(man.getName(), "fulljulia")


if __name__ == '__main__':
    unittest.main()
