class Config:
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
        self.fractals = {
            'mandelbrot': {
                'centerX': -0.6,
                'centerY': 0.0,
                'axisLen': 2.5,
                'type': 'mandelbrot'
            },

            'spiral0': {
                'centerX': -0.761335372924805,
                'centerY': 0.0835704803466797,
                'axisLen': 0.004978179931102462,
                'type': 'mandelbrot'
            },

            'spiral1': {
                'centerX': -0.747,
                'centerY': 0.1075,
                'axisLen': 0.002,
                'type': 'mandelbrot'
            },

            'seahorse': {
                'centerX': -0.745,
                'centerY': 0.105,
                'axisLen': 0.01,
                'type': 'mandelbrot'
            },

            'elephants': {
                'centerX': 0.30820836067024604,
                'centerY': 0.030620936230004017,
                'axisLen': 0.03,
                'type': 'mandelbrot'
            },

            'leaf': {
                'centerX': -1.543577002,
                'centerY': -0.000058690069,
                'axisLen': 0.000051248888,
                'type': 'mandelbrot'
            },
            'fulljulia': {
                'centerX': 0.0,
                'centerY': 0.0,
                'axisLen': 4.0,
                'type': 'julia'
            },

            'hourglass': {
                'centerX': 0.618,
                'centerY': 0.00,
                'axisLen': 0.017148277367054,
                'type': 'julia'
            },

            'lakes': {
                'centerX': -0.339230468501458,
                'centerY': 0.417970758224314,
                'axisLen': 0.164938488846612,
                'type': 'julia'
            },
        }

    def getFractal(self, name):
        """
        returns the type of fractal the image is.
        """
        if name in self.fractals:
            return self.fractals[name]['type']

    def getImageType(self, name):
        """
        returns the image
        """
        if name in self.fractals:
            return name

    def getImageInformation(self, info, image):
        """
        returns the specified information in the fractal image.
        """
        return self.fractals[image][info]

    def getListOfFractalImages(self):
        """
        returns a full list of all the Fractal Images.
        """
        myList = []
        for i in self.fractals:
            myList.append(i)
        return myList

