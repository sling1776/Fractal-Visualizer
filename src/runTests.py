import unittest

from Testing import testFractal, testGradient, testFractalFactory, testGradientFactory


suite = unittest.TestSuite()
tests = (testFractalFactory.TestFractalFactory, testFractal.TestFractal, testGradientFactory.TestGradientFactory, testGradient.TestGradient)

for test in tests:
    suite.addTest(unittest.makeSuite(test))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
