from tkinter import Tk, Canvas, PhotoImage, mainloop


class ImagePainter():
    """
        Stores the width and height of the Tkinter window. It creates the window and
        creates the image of the fractal. It also has the option to save the image.
        """

    def __init__(self, width, height, fractal):
        """
        stores the width and height. It also calls setUpGUI to create a ne Tkinter
        window. It also stores the fractal that is going to be used to create the
        image.
        """
        self.width = width
        self.height = height
        self.fractal = fractal
        self.window = Tk()
        self.img = PhotoImage(width=512, height=512)
        self.setUpGUI()

    def setUpGUI(self):
        """
        sets up a new tkinter window given the width and height.
        """
        WHITE = '#ffffff'
        # Set up the GUI so that we can paint the fractal image on the screen
        canvas = Canvas(self.window, width=self.width, height=self.height, bg=WHITE)
        canvas.pack()
        canvas.create_image((256, 256), image=self.img, state="normal")


    def makeImage(self):
        """
        takes a Fractal Object and creates the image. Calls makeRow() repeatedly and
        updates the image after every call.
        """
        for row in range(512, 0, -1):
            self.makeRow(row)
            self.window.update()  # display a row of pixels

    def makeRow(self, row):
        """
        Takes a fractal and calculates the colors of each pixel in a row by calling the
        Fractal Objects calculateColor method.
        """
        for col in range(512):
            color = self.fractal.calculateColor(row, col)
            self.img.put(color, (col, 512 - row))


    def saveImage(self):
        """
        gets the name from the fractal and then saves the image as a PNG to the CWD.
        """
        # Save the image as a PNG
        self.img.write(f"{self.fractal.getName()}.png")
        print(f"Wrote image {self.fractal.getName()}.png")

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height
