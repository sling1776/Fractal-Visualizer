import unittest
from Gradient import Gradient
from Mandelbrot import Mandelbrot


# autocmd BufWritePost <buffer> !python3 runTests.py

class TestMandelbrot(unittest.TestCase):
    def test_colorOfThePixelMandelbrot(self):
        gradient = Gradient()
        man = Mandelbrot("mandelbrot", gradient, -1.85, .65, -1.25)
        self.assertEqual(man.calculateColor(0, 0), "#ffe4b5")
        self.assertEqual(man.calculateColor(10, 10), "#ffe4b5")
        self.assertEqual(man.calculateColor(20, 20), "#ffe4b5")
        self.assertEqual(man.calculateColor(300, 300), "#002277")
        self.assertEqual(man.calculateColor(512, 512), "#ffe5b2")
        self.assertEqual(man.calculateColor(1000, 1000), "#ffe4b5")


    def test_colorOfThePixelSpiral0(self):
        gradient = Gradient()
        man = Mandelbrot("spiral0", gradient, -0.7638244628903562, -0.7588462829592538, 0.08108139038112847 )
        self.assertEqual(man.calculateColor(0, 0), "#002277")
        self.assertEqual(man.calculateColor(10, 10), "#002277")
        self.assertEqual(man.calculateColor(20, 20), "#002277")
        self.assertEqual(man.calculateColor(300, 300), "#0073a2")
        self.assertEqual(man.calculateColor(512, 512), "#6cff40")
        self.assertEqual(man.calculateColor(1000, 1000), "#85ff4a")

    def test_colorOfThePixelSpiral1(self):
        gradient = Gradient()
        man = Mandelbrot("spiral1", gradient, -0.748, -0.746, 0.1065)
        self.assertEqual(man.calculateColor(0, 0), "#002277")
        self.assertEqual(man.calculateColor(10, 10), "#002277")
        self.assertEqual(man.calculateColor(20, 20), "#002277")
        self.assertEqual(man.calculateColor(300, 300), "#002277")
        self.assertEqual(man.calculateColor(512, 512), "#002277")
        self.assertEqual(man.calculateColor(1000, 1000), "#002277")

    def test_colorOfThePixelSeahorse(self):
        gradient = Gradient()
        man = Mandelbrot("seahorse", gradient, -0.75, -0.74, 0.09999999999999999)
        self.assertEqual(man.calculateColor(0, 0), "#85ff4a")
        self.assertEqual(man.calculateColor(10, 10), "#7dff47")
        self.assertEqual(man.calculateColor(20, 20), "#47ff33")
        self.assertEqual(man.calculateColor(300, 300), "#00de9e")
        self.assertEqual(man.calculateColor(512, 512), "#002277")
        self.assertEqual(man.calculateColor(1000, 1000), "#002277")

    def test_colorOfThePixelElephants(self):
        gradient = Gradient()
        man = Mandelbrot("elephants", gradient, 0.293208360670246, 0.32320836067024605, 0.015620936230004018)
        self.assertEqual(man.calculateColor(0, 0), "#95ff51")
        self.assertEqual(man.calculateColor(10, 10), "#a4ff58")
        self.assertEqual(man.calculateColor(20, 20), "#b9ff62")
        self.assertEqual(man.calculateColor(300, 300), "#002277")
        self.assertEqual(man.calculateColor(512, 512), "#a4ff58")
        self.assertEqual(man.calculateColor(1000, 1000), "#00d4ab")

    def test_colorOfThePixelLeaf(self):
        gradient = Gradient()
        man = Mandelbrot("leaf", gradient, -1.543602626444, -1.543551377556, -8.4314513e-05)
        self.assertEqual(man.calculateColor(0, 0), "#ddff76")
        self.assertEqual(man.calculateColor(10, 10), "#ddff76")
        self.assertEqual(man.calculateColor(20, 20), "#ddff76")
        self.assertEqual(man.calculateColor(300, 300), "#b9ff62")
        self.assertEqual(man.calculateColor(512, 512), "#c6ff68")
        self.assertEqual(man.calculateColor(1000, 1000), "#bfff65")

    def test_getNameMandelbrot(self):
        grad = Gradient
        man = Mandelbrot("mandelbrot", grad, 0, 0, 0)
        self.assertEqual(man.getName(), "mandelbrot")


if __name__ == '__main__':
    unittest.main()
