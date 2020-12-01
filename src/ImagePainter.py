from tkinter import Tk, Canvas, PhotoImage
from GradientFactory import GradientFactory

class ImagePainter:
    """
    Stores the width and height of the Tkinter window. It creates the window and
    creates the image of the fractal. It also has the option to save the image.
    """

    def __init__(self, fractal, gradient):
        """
        stores the width and height. It also calls setUpGUI to create a new Tkinter
        window. It also stores the fractal that is going to be used to create the
        image.
        """
        self.width = fractal.getWidth()
        self.height = fractal.getHeight()
        self.fractal = fractal
        self.window = Tk()
        self.img = PhotoImage(width=self.width, height=self.height)
        self.setUpGUI()
        self.grad = self.developGradient(gradient)

    def setUpGUI(self):
        """
        sets up a new tkinter window given the width and height.
        """
        WHITE = '#ffffff'
        # Set up the GUI so that we can paint the fractal image on the screen
        canvas = Canvas(self.window, width=self.width, height=self.height, bg=WHITE)
        canvas.pack()
        canvas.create_image((self.width/2, self.height/2), image=self.img, state="normal")

    def makeImage(self):
        """
        takes a Fractal Object and creates the image. Calls makeRow() repeatedly and
        updates the image after every call.
        """

        for row in range(self.height):
            self.makeRow(row)
            self.window.update()  # display a row of pixels

    def makeRow(self, row):
        """
        Takes a fractal and calculates the colors of each pixel in a row by calling the
        Fractal Objects calculateColor method.
        """
        for col in range(self.width):
            count = self.fractal.calculateIterations(row, col)
            color = self.grad.getColor(count)
            self.img.put(color, (col, row))

    def saveImage(self, fileName="mandelbrot.frac"):
        """
        gets the name from the fractal and then saves the image as a PNG to the CWD.
        """
        # Save the image as a PNG
        if fileName == "":
            fileName = "mandelbrot.frac"
        directories = fileName.split("/")
        for n in directories:
            if ".frac" in n:
                name = n.rsplit(".", 1)[0]
        self.img.write(f"{name}.png")
        print(f"Wrote image {name}.png")

    def developGradient(self, gradient):
        return GradientFactory().makeGradient(gradient, self.fractal.MAX_ITERATIONS)

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height
