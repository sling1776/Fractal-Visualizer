import unittest
from GradientFactory import GradientFactory
from GradientFiles import Greyscale, Gradient, BlueGreen, RedToWhite, StandGradient, threeColor
import os

class TestGradientFactory(unittest.TestCase):

    fac = GradientFactory()

    def test_makeGradient(self):
        myList = ["standgradient", "redtowhite", "greyscale", "bluegreen", "threecolor"]
        myList2 = [StandGradient.StandGradient, RedToWhite.RedToWhite, Greyscale.Greyscale, BlueGreen.BlueGreen, threeColor.ThreeColor]
        for i in range(len(myList)):
            self.assertIsInstance(self.fac.makeGradient(myList[i], 10), myList2[i])


if __name__ == '__main__':
    unittest.main()