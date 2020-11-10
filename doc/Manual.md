# Fractal Visualizer User Manual

**Introduction**

The Fractal Visualizer allows the user to see various parts of the fractal. This
program is run on a commandline interface. after a command is entered it will 
open a new window that will draw an image of the chosen fractal. It will then 
automatically save the image to the current working directory (CWD).

**Instructions For Use**

To use this program, open a terminal and navigate into the src/ folder of the 
repository. From there enter into the terminal:
    
    $ python main.py [FRACTAL]
    
Replace FRACTAL with any of these commands:
    
    fulljulia
	hourglass
	lakes
	mandelbrot
	spiral0
	spiral1
	seahorse
	elephants
	leaf
	
Do not close the window that pops up. It will take sometime for the program to create 
the image. Once the image is complete, it will save the file to the src/ directory or 
wherever your CWD is. 

**Common Error Messages**

*1. Misspelled or invalid argument:*
When attempting to run the program, it is common for the user to misspell the fractal
image they want created. The program will only accept the following case-sensitive 
arguments:
    
    fulljulia
	hourglass
	lakes
	mandelbrot
	spiral0
	spiral1
	seahorse
	elephants
	leaf

If another argument is entered or if an argument is misspelled the output on the console will 
look like this:

    $ python main.py moustache
      ERROR: moustache is not a valid fractal
      Please choose one of the following:
              mandelbrot
              spiral0
              spiral1
              seahorse
              elephants
              leaf
              fulljulia
              hourglass
              lakes


The program will then close and the user can rerun the program this time giving it a correct
argument. 

*2. Missing Argument:*
If the user neglects adding a desired fractal argument to the command the console output will
look this this:
    
    $ python main.py
      Please provide the name of a fractal as an argument
            mandelbrot
            spiral0
            spiral1
            seahorse
            elephants
            leaf
            fulljulia
            hourglass
            lakes

It will then exit the program without creating any images. All this means is the user 
needs to add the name of a fractal after the command:
    
    $ python main.py [FRACTAL]

For example:

    $ python main.py mandelbrot
    





