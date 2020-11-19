import sys
from Config import Config
from ImagePainter import ImagePainter
from FractalFactory import FractalFactory
from tkinter import mainloop

'''
This is the main Driver Program. It checks for valid input and then creates the image.
'''

if __name__ == '__main__':
    config = Config()
    # if len(sys.argv) < 2:
    #     print("Please provide the name of a fractal as an argument")
    #     for i in config.getListOfFractalImages():
    #         print(f"\t{i}")
    #     sys.exit(1)
    #
    # elif sys.argv[1] not in config.getListOfFractalImages():
    #     print(f"ERROR: {sys.argv[1]} is not a valid fractal")
    #     print("Please choose one of the following:")
    #     for i in config.getListOfFractalImages():
    #         print(f"\t{i}")
    #     sys.exit(1)
    #
    # else:
    #     image = sys.argv[1]
    if len(sys.argv) == 2:
        image = sys.argv[1]
    else:
        image = ""

    fracFac = FractalFactory()
    fractal = fracFac.makeFractal(image)
    painter = ImagePainter(fractal)

    painter.makeImage()
    #painter.saveImage()
    # make the window stay open.
    mainloop()

