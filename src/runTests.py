import unittest

from Testing import TestIntegration, TestMandelbrot, TestJulia, TestConfig, TestGradient


suite = unittest.TestSuite()
tests = (TestConfig.TestConfig, TestGradient.TestGradient, TestJulia.TestJulia, TestMandelbrot.TestMandelbrot,TestIntegration.TestIntegration)

for test in tests:
    suite.addTest(unittest.makeSuite(test))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
