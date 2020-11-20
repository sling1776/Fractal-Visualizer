import sys
from ImagePainter import ImagePainter
from FractalFactory import FractalFactory
from tkinter import mainloop

'''
This is the main Driver Program. It checks for valid input and then creates the image.
'''

if __name__ == '__main__':
    if len(sys.argv) == 2:
        image = sys.argv[1]
        grad = ""
    elif len(sys.argv) >= 3:
        image = sys.argv[1]
        grad = sys.argv[2].lower()
    else:
        image = ""
        grad = ""



    fracFac = FractalFactory()
    fractal = fracFac.makeFractal(image)
    painter = ImagePainter(fractal, grad)

    painter.makeImage()
    #painter.saveImage()
    # make the window stay open.
    mainloop()

