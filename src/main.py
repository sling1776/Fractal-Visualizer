import sys
from Config import Config
from ImagePainter import ImagePainter
from Julia import Julia
from Mandelbrot import Mandelbrot
from Gradient import Gradient
from tkinter import mainloop

'''
This is the main Driver Program. It checks for valid input and then creates the image.
'''

if __name__ == '__main__':
    config = Config()
    if len(sys.argv) < 2:
        print("Please provide the name of a fractal as an argument")
        for i in config.getListOfFractalImages():
            print(f"\t{i}")
        sys.exit(1)

    elif sys.argv[1] not in config.getListOfFractalImages():
        print(f"ERROR: {sys.argv[1]} is not a valid fractal")
        print("Please choose one of the following:")
        for i in config.getListOfFractalImages():
            print(f"\t{i}")
        sys.exit(1)

    else:
        image = sys.argv[1]
    # determine Fractal Type
    fracType = config.getFractal(image)
    # get configuration data from dictionary
    cenX = config.getImageInformation('centerX', fracType, image)
    cenY = config.getImageInformation('centerY', fracType, image)
    axislen = config.getImageInformation('axisLen', fracType, image)
    # calculate needed info
    minx = cenX - (axislen / 2.0)
    maxx = cenX + (axislen / 2.0)
    miny = cenY - (axislen / 2.0)
    gradient = Gradient()
    if fracType == "julia":
        fractal = Julia(image, gradient, minx, maxx, miny)
    else:
        fractal = Mandelbrot(image, gradient, minx, maxx, miny)
    # make Tkinter window.
    painter = ImagePainter(512, 512, fractal)

    painter.makeImage()
    painter.saveImage()
    # make the window stay open.
    mainloop()

