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
        
        

**Design a process for obtaining the output from the input.  Consider both *good*
and *bad* inputs.  Find or create examples of both kinds of input.**

**Work out problem examples on paper, on a whiteboard or some other medium that
is *not* your computer.  It is a mistake to begin writing executable code
before you thoroughly understand what form the algorithm(s) must take.**

**Instead, describe components of the system in *"pseudocode"*.  Expect to make
lots of mistakes at this point.  You will find that it is much easier to throw
away pseudocode than real code.**

**Manually work through several examples that illustrate the program's overall
purpose, as well as the purpose of each component of the finished system.  You
will converge on a correct solution much faster if you feel comfortable making
mistakes as you go.**

**This phase involves the use of many levels of abstraction to decompose the
problem into manageable components, and design strategies for implementing each
component.  Components may be functions, modules or classes.**


# 3.  Function Template

**Combine the function stubs written in step #2 with pseudocode from step #3.
Comment out the pseudocode, leaving a valid program that compiles/runs without
errors.  At this stage your program doesn't quite work, but it also doesn't
crash.**


# 4.  Implementation

**This is the only part of the process focused on writing code in your chosen
programming language.**

**One by one translate passages of pseudocode into valid code.  Fill in the gaps
in the function template.  Exploit the purpose statement and the examples.**

**If you were thorough in the previous steps and are familiar with your
programming system this part will go by very quickly and the code will write
itself.**

**When you are learning a new programming language or an unfamiliar library this
phase can be slow and difficult.  As you gain experience with the relevant
technologies you will spend less and less time in this phase of the process.**


# 5.  Testing

**Articulate the examples given in step #2 as tests and ensure that each
function passes all of its tests.  Doing so discovers mistakes.  Tests also
supplement examples in that they help others read and understand the definition
when the need arises—and it will arise for any serious program.**

**As bugs are discovered and fixed, devise new test cases that will detect these
problems should they return.**

**If you didn't come across any bugs (lucky you!) think of a possible flaw and a
test that can be employed to screen for it.**

**At a minimum you should create a document explaining step-by-step how a
non-technical user may manually test your program to satisfy themselves that it
operates correctly.  Explain the entire process starting how to launch the
program, what inputs they should give and what results they should see at every
step.  Provide test cases of good and bad inputs to catch both false positives
and false negatives.  Any deviation from the expected outputs are errors.**

**The ideal is to write an automated test to avoid all manual labor beyond
launching the test.**
