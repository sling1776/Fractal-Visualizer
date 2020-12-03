import unittest
from GradientFiles import BlueGreen, Gradient, Greyscale, RedToWhite, StandGradient, threeColor


class TestGradient(unittest.TestCase):
    bg = BlueGreen.BlueGreen(10)
    grey = Greyscale.Greyscale(10)
    red = RedToWhite.RedToWhite(10)
    stand = StandGradient.StandGradient(10)
    three = threeColor.ThreeColor(10)
    def test_getColor_bg(self):
        self.assertEqual(self.bg.getColor(0), "#0000ff")
        self.assertEqual(self.bg.getColor(5), "#00b8a4")
        self.assertEqual(self.bg.getColor(9), "#008000")

    def test_getColor_grey(self):
        self.assertEqual(self.grey.getColor(0), "#ffffff")
        self.assertEqual(self.grey.getColor(5), "#717171")
        self.assertEqual(self.grey.getColor(9), "#000000")

    def test_getColor_red(self):
        self.assertEqual(self.red.getColor(0), "#620000")
        self.assertEqual(self.red.getColor(5), "#cc7b7b")
        self.assertEqual(self.red.getColor(9), "#ffffff")

    def test_getColor_stand(self):
        self.assertEqual(self.stand.getColor(0), "#ffe4b5")
        self.assertEqual(self.stand.getColor(5), "#05ff5b")
        self.assertEqual(self.stand.getColor(9), "#002277")

    def test_getColor_three(self):
        self.assertEqual(self.three.getColor(0), "#ff0000")
        self.assertEqual(self.three.getColor(5), "#800080")
        self.assertEqual(self.three.getColor(9), "#0000ff")





if __name__ == '__main__':
    unittest.main()