import unittest

from Testing import TestMandelbrot, TestJulia, TestIntegration


suite = unittest.TestSuite()
tests = (TestMandelbrot.TestMandelbrot, TestJulia.TestJulia, TestIntegration.TestIntegration)
for test in tests:
    suite.addTest(unittest.makeSuite(test))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
