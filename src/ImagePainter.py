from tkinter import Tk, Canvas, PhotoImage, mainloop


class ImagePainter():
    """
        Stores the width and height of the Tkinter window. It creates the window and
        creates the image of the fractal. It also has the option to save the image.
        """

    def __init__(self, width, height):
        """
        stores the width and height. It also calls setUpGUI to create a ne Tkinter
        window. It also stores the fractal that is going to be used to create the
        image.
        """
        self.width = width
        self.height = height

    def setUpGUI(self):
        """
        sets up a new tkinter window given the width and height.
        """
        # Set up the GUI so that we can paint the fractal image on the screen
        window = Tk()
        img = PhotoImage(width=512, height=512)
        paint(images, image)

        # Save the image as a PNG
        img.write(f"{image}.png")
        print(f"Wrote image {image}.png")

        # Call tkinter.mainloop so the GUI remains open
        mainloop()

        # Display the image on the screen
        canvas = Canvas(window, width=512, height=512, bg='#ffffff')
        canvas.pack()
        canvas.create_image((256, 256), image=img, state="normal")

    def makeImage(self):
        """
        takes a Fractal Object and creates the image. Calls makeRow() repeatedly and
        updates the image after every call.
        """
        for row in range(512, 0, -1):
            for col in range(512):
                # x = minx + col * pixelsize
                # y = miny + row * pixelsize
                # color = colorOfThePixel(complex(x, y), gradient)
                img.put(color, (col, 512 - row))
            window.update()  # display a row of pixels

    def makeRow(self, column):
        """
        Takes a fractal and calculates the colors of each pixel in a row by calling the
        Fractal Objects calculateColor method.
        """
        for col in range(512):
            # x = minx + col * pixelsize
            # y = miny + row * pixelsize
            # color = colorOfThePixel(complex(x, y), gradient)
            img.put(color, (col, 512 - row))
        window.update()  # display a row of pixels

    def saveImage(self):
        """
        gets the name from the fractal and then saves the image as a PNG to the CWD.
        """

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height
