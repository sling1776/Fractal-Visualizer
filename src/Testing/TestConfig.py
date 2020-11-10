import unittest
from Config import Config


# autocmd BufWritePost <buffer> !python3 runTests.py

class TestConfig(unittest.TestCase):
    config = Config()
    def test_getFractal(self):
        self.assertEqual(self.config.getFractal("mandelbrot"), "mandelbrot")
        self.assertEqual(self.config.getFractal("spiral0"), "mandelbrot")
        self.assertEqual(self.config.getFractal("spiral1"), "mandelbrot")
        self.assertEqual(self.config.getFractal("seahorse"), "mandelbrot")
        self.assertEqual(self.config.getFractal("elephants"), "mandelbrot")
        self.assertEqual(self.config.getFractal("leaf"), "mandelbrot")
        self.assertIsNone(self.config.getFractal("HeyBabe"))

    def test_getImageType(self):
        self.assertEqual(self.config.getImageType("leaf","mandelbrot"), "leaf")
        self.assertEqual(self.config.getImageType("lakes", "julia"), "lakes")
        self.assertIsNone(self.config.getImageType("leaf","julia"))

    def test_getListOfFractalImages(self):
        list = ["mandelbrot", "spiral0", "spiral1", "seahorse",
                "elephants", "leaf", "fulljulia", "hourglass", "lakes"]
        self.assertEqual(self.config.getListOfFractalImages(), list)

    def test_getImageInformation(self):
        self.assertEqual(self.config.getImageInformation("centerX","mandelbrot","mandelbrot"), -0.6)
        self.assertEqual(self.config.getImageInformation("axisLen", "julia", "lakes"), 0.164938488846612)
        self.assertEqual(self.config.getImageInformation("centerY", "julia", "fulljulia"), 0)



if __name__ == '__main__':
    unittest.main()