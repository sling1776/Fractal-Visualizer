import unittest

from Testing import TestIntegration


suite = unittest.TestSuite()
test = (TestIntegration.TestIntegration)
# TestMandelbrot.TestMandelbrot, TestJulia.TestJulia,
# for test in tests:
suite.addTest(unittest.makeSuite(test))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
