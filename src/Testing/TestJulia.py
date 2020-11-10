import unittest
from Julia import Julia
from Gradient import Gradient


# autocmd BufWritePost <buffer> !python3 runTests.py

class TestJulia(unittest.TestCase):

    def test_colorOfThePixelFulljulia(self):
        gradient = Gradient()
        man = Julia("fulljulia", gradient, -2.0, 2.0, -2.0)
        self.assertEqual(man.calculateColor(0, 0), "#ffe4b5")
        self.assertEqual(man.calculateColor(10, 10), "#ffe4b5")
        self.assertEqual(man.calculateColor(20, 20), "#ffe4b5")
        self.assertEqual(man.calculateColor(300, 300), "#009cb3")
        self.assertEqual(man.calculateColor(512, 512), "#ffe4b5")
        self.assertEqual(man.calculateColor(1000, 1000), "#ffe4b5")

    def test_colorOfThePixelHourglass(self):
        gradient = Gradient()
        man = Julia("hourglass", gradient, 0.609425861316473, 0.626574138683527, -0.008574138683527)
        self.assertEqual(man.calculateColor(0, 0), "#009cb3")
        self.assertEqual(man.calculateColor(10, 10), "#009cb3")
        self.assertEqual(man.calculateColor(20, 20), "#009cb3")
        self.assertEqual(man.calculateColor(300, 300), "#009cb3")
        self.assertEqual(man.calculateColor(512, 512), "#009cb3")
        self.assertEqual(man.calculateColor(1000, 1000), "#009cb3")

    def test_colorOfThePixelLakes(self):
        gradient = Gradient()
        man = Julia("hourglass", gradient, -0.421699712924764, -0.256761224078152, 0.335501513801008)
        self.assertEqual(man.calculateColor(0, 0), "#ffefa1")
        self.assertEqual(man.calculateColor(10, 10), "#ffefa1")
        self.assertEqual(man.calculateColor(20, 20), "#ffefa1")
        self.assertEqual(man.calculateColor(300, 300), "#fff797")
        self.assertEqual(man.calculateColor(512, 512), "#ffeaa8")
        self.assertEqual(man.calculateColor(1000, 1000), "#ffefa1")

    def test_getNameJulia(self):
        grad = Gradient
        man = Julia("fulljulia", grad, 0, 0, 0)
        self.assertEqual(man.getName(), "fulljulia")


if __name__ == '__main__':
    unittest.main()
