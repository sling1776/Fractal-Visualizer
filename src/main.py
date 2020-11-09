import sys
from Config import Config
from ImagePainter import ImagePainter
from Julia import Julia
from Mandelbrot import Mandelbrot
from Gradient import Gradient
from tkinter import mainloop

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

    fracType = config.getFractal(image)
    gradient = Gradient()
    cenX = config.getImageInformation('centerX', fracType, image)
    cenY = config.getImageInformation('centerY', fracType, image)
    axislen = config.getImageInformation('axisLen', fracType, image)

    minx = cenX - (axislen / 2.0)
    maxx = cenX + (axislen / 2.0)
    miny = cenY - (axislen / 2.0)

    if fracType == "julia":
        fractal = Julia(image, gradient, minx, maxx, miny)
    else:
        fractal = Mandelbrot(image, gradient, minx, maxx, miny)

    painter = ImagePainter(512, 512, fractal)
    # TODO: Spencer this make image call probably belongs in main.py
    painter.makeImage()
    painter.saveImage()
    # Call tkinter.mainloop so the GUI remains open
    mainloop()

