# Fractal Visualizer User Manual

**Introduction**

The Fractal Visualizer allows the user to see various parts of the fractal. This
program is run on a commandline interface. after a command is entered it will 
open a new window that will draw an image of the chosen fractal. It will then 
automatically save the image to the current working directory (CWD).

**Instructions For Use**

To use this program, open a terminal and navigate into the src/ folder of the 
repository. From there enter into the terminal:
    
    $ python main.py [optional-FRACTAL_FILE [optional-GRADIENT]]
    
The program has a default image it will create for you by just running the program
it will make that image automatically. You can give the program a .frac file to read
by entering the name of the FRACTAL_FILE in reference to your current working directory.

You also have the option to replace GRADIENT with any of these commands:
    
    standgradient
    redtowhite
    greyscale
    bluegreen
    threecolor
    
This will change the colors that are displayed on the fractal image. "standgradient"
is the default color scheme that is used. When GRADIENT is not supplied, the program 
will default to this scheme. 
	
Do not close the window that pops up. It will take sometime for the program to create 
the image. Once the image is complete, it will save the file to the src/ directory or 
wherever your CWD is. 

**Common Error Messages**

*1. Misspelled or invalid GRADIENT argument:*
When attempting to run the program, it is common for the user to misspell the color gradient
they want created. The program will only accept the following non-case-sensitive arguments:
    
    standgradient
    redtowhite
    greyscale
    bluegreen
    threecolor

If another argument is entered or if an argument is misspelled the program will raise a NotImplementedError.

    $ python src/main.py data/funnel-down.frac NOT_EXIST
    Traceback (most recent call last):
      File "src/main.py", line 27, in <module>
        gradient = GradientFactory.makeGradient(fractal.iterations, gtype=gradient)
      File "/home/fadein/school/Sp19/cs1440/Assn/6/src/GradientFactory.py", line 49, in makeGradient
        raise NotImplementedError("Invalid gradient requested")
    NotImplementedError: Invalid gradient requested



The program will then close and the user can rerun the program this time giving it a correct
argument. 

*2. Unknown File:*
If the user enters a file that does not exist in relation to the CWD, the program will raise a 
FileNotFoundError:
    
    $ python src/main.py data/NOT_EXIST ColorCube
    Traceback (most recent call last):
      File "src/main.py", line 26, in <module>
        fractal = FractalFactory.makeFractal(cfg)
      File "/home/fadein/school/Sp19/cs1440/Assn/6/src/FractalFactory.py", line 30, in makeFractal
        cfg = __readConfig(cfgFile)
      File "/home/fadein/school/Sp19/cs1440/Assn/6/src/FractalFactory.py", line 64, in __readConfig
        with open(cfgFile) as f:
    FileNotFoundError: [Errno 2] No such file or directory: 'data/NOT_EXIST'


It will then exit the program without creating any images. All this means is the user 
needs to add the valid name of a fractal after the command:
    
    $ python main.py [FRACTAL_FILE]

For example:

    $ python src/main.py data/mandelbrot.frac
    
*2. Invalid Fractal File:*

It the file given to the program is not a valid fractal file and is missing information or
has invalid information, the program will raise a NotImplementedError.

    $ python src/main.py data/invalid.frac threecoloR
    Traceback (most recent call last):
      File "src/main.py", line 24, in <module>
        fractal = fracFac.makeFractal(image)
      File "C:\Users\DELL\cs1440-lingwall-spencer-assn4\src\FractalFactory.py", line 34, in makeFractal
        fractal = Mandelbrot(dic)
      File "C:\Users\DELL\cs1440-lingwall-spencer-assn4\src\FractalFiles\Mandelbrot.py", line 8, in __init__
        self.checkDictionary(dictionary)
      File "C:\Users\DELL\cs1440-lingwall-spencer-assn4\src\FractalFiles\Fractal.py", line 41, in checkDictionary
        raise NotImplementedError("Invalid Fractal File: iterations must be integer")
    NotImplementedError: Invalid Fractal File: iterations must be integer
    
At the end of the message the program will inform the user what is wrong with the fractal File. 
    





