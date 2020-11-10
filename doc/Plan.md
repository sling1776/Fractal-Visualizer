*Replace the bold text with your own content*

*Adapted from https://htdp.org/2020-5-6/Book/part_preface.html*

# 0.  From Problem Analysis to Data Definitions
The issue that I have is to refactor this program to be a Program System's Product. I 
am going to be redesigning the basic structure of the files essentially getting rid of 
the two given files and replacing them with 6 other files. 

Prior to Designing it, I will go through the code and ensure that there are no obvious 
errors or ambiguities in the code that need to be removed and won't change the flow of the
program. basically it is just removing nonessential things:

This is the order I removed and changed lines in the files. the file line numbers change as the file changed.

Julia_fractal.py:
    These lines found in the file src/julia_fractal.py at line 41 are overly complex:
    ```
        for key in dictionary:
            if key in dictionary:
                if key == name:
                    value = dictionary[key]
                    return key
    ```
    It can be replaced without changing the meaning of the program to:
    ```
    for key in dictionary:
        if key == name:
            return key
    ```   
    line 26 and 29 in the file src/julia_fractal.py are is unreachable. 
    ```
    z += z + c  
    ...    
    return grad[78]
    ```
    simply removed the lines.
    lines 68-76 are repetitive as well as unused. 
    ```
        canvas.pack()  # This seems repetitive
        canvas.pack()  # But it is how Larry wrote it
        canvas.pack()  # Larry's a smart guy.  I'm sure he has his reasons.
        area_in_pixels = 512 * 512
        canvas.pack()  # Does this even matter?
        # At this scale, how much length and height of the
        # imaginary plane does one pixel cover?
    ```
    simply removed the lines.   
    line 71-72 are repetitive and unused:
    ```
    fraction = int(512 / 64)
    canvas.pack()
    ```
    removed lines
    
mbrot_fractal.py:
    line 48 in mbrot_fractal.py is extra. it never gets reached.
    ```
    return gradient[MAX_ITERATIONS]
    ```
    removed line
    line 64 declares a variable that is never used. 
    ```
    maxy = fractal['centerY'] + (fractal['axisLen'] / 2.0)
    ```
    removed line
    line 75-76 declare variable never used:
    ```
    portion = int(512 / 64)
    total_pixels = 1048576
    ```
    removed lines
    
Dead code and useless code should be removed at this point. 
There are still many other issues with the code that will be changed as needed. 

# 1.  System Analysis

Class ImagePainter():
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
    def setUpGUI(self):
        """
        sets up a new tkinter window given the width and height.
        """
    def makeImage(self):
        """
        takes a Fractal Object and creates the image. Calls makeRow() repeatedly and 
        updates the image after every call.
        """
    def makeRow(self, column):
        """
        Takes a fractal and calculates the colors of each pixel in a row by calling the
        Fractal Objects calculateColor method. 
        """
    def saveImage(self):
        """
        gets the name from the fractal and then saves the image as a PNG to the CWD.
        """
    def getWidth():
    def getHeight():
    
Class Fractal():
    """
    Is a parent class for the mandlebrot and julia classes. It uses the Config object
    to determine its minX, minY and maxX. It can calculate the color of a pixel and
    can calculate the needed complex numbers to get the color.
    """
    def __init__(self, name, gradient, minX, maxX, minY):
        """
        stores name and min/max data. Stores Gradient.
        """
    def calculateColor():
        """
        calculates the color of a given pixel
        """
    def calculateComplexNumber():
        """
        calcualtes the needed complex numbers for color calculations
        """
    def getName():
    
Class Mandelbrot(Fractal):
    """
    Is an extention of Fractal. Overwrites a single complex number.
    """
    def __init__(self, name gradient, minX, maxX, minY):
        """
        Essentially copied from Fractal. just add a new variable complexNumber.
        """

Class Julia(Fractal):
    """
    Is an extention of Fractal. Overwrites a single complex number.
    """
    def __init__(self, name gradient, minX, maxX, minY):
        """
        Essentially copied from Fractal. just add a new variable complexNumber.
        """
        
Class Config():
    """
    Primarily is used to set up either a julia Fractal or a Mandlebrot Fractal
    contains a Dictionary with all the needed information about each one. Basically
    it is a three deep dictionary. Type of fractal, Type of image, Configuration
    data for it.
    """
    def __init__(self):
        """
        creates the dictionary
        """
    def getFractal():
    def getImageType():
    def getImageInformation():
    
Class Gradient():
    """
    contains an array with all the colors in it.
    """
    def __init__(self):
        """
        create color array.
        """
    def getColor(self, iterations):
    def getlength
    
Class main():
    """
    is the main driver for the program. Creates gradient, Config, fractal and 
    ImagePainter Objects. It then runs the program
    """
    def __init__(self):
        """
        create needed objects
        """
    def run():
        """
        runs the program.
        """

# 2.  Functional Examples

Class ImagePainter:
    setUpGUI:
        create GUI
        make image
        make canvas and pack it to the GUI
    save image
        open a new file
        write image to the file
    makeimage
        call makeRow
    makeRow
        call calculate color from the fractal object
        make the row with the colors. 
        update the row in the GUI
    getWidth
    GetHeight
    getPixelSize
    
Class Fractal
    calculateColor
        will calculate the number of iterations needed.  
        return that number
    calculateComplexNumber
        calculate the needed complex number
        return it
    getName()
    
Class Config
    getImageInformation
    getImage
    getFractal
    
Class Gradient
    getColor
        

# 3.  Function Template


# 4.  Implementation

Done

# 5.  Testing

To test the file, simply navigate to the src/ directory and type in the commandline:
    $ python runTests.py
The tests will run themselves. You will notice that in the TestImplementation it is skipped.
If you would like to test the implementation in addition to the functionality I have made it easy 
for you. from the src/ directory type in the following commands:
    $ cd Testing/TestDocs/NewPics
    $ chmod +x  makePics.sh
    $ ./makePics.sh
These commands in order are:
1. change the directory
2. allow makePics.sh to run on the shell.
3. run makePics.sh

makePics.sh changes the main.py program briefly so it can run through all the various commands quickly
without user interference. It then runs through all the commands that could be seen creating new 
pictures for all the different types of fractals.

Once it is done running through all the commands, you can navigate back to the src/ directory and run
    $ python runTests.py 
This time you will see that the TestImplementation did not get skipped and that it passed. 
