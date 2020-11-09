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
            'mandlebrot': {
                'mandelbrot': {
                    'centerX': -0.6,
                    'centerY': 0.0,
                    'axisLen': 2.5,
                },

                'spiral0': {
                    'centerX': -0.761335372924805,
                    'centerY': 0.0835704803466797,
                    'axisLen': 0.004978179931102462,
                },

                'spiral1': {
                    'centerX': -0.747,
                    'centerY': 0.1075,
                    'axisLen': 0.002,
                },

                'seahorse': {
                    'centerX': -0.745,
                    'centerY': 0.105,
                    'axisLen': 0.01,
                },

                'elephants': {
                    'centerX': 0.30820836067024604,
                    'centerY': 0.030620936230004017,
                    'axisLen': 0.03,
                },

                'leaf': {
                    'centerX': -1.543577002,
                    'centerY': -0.000058690069,
                    'axisLen': 0.000051248888,
                },
            },
            'julia': {
                'fulljulia': {
                    'centerX': 0.0,
                    'centerY': 0.0,
                    'axisLen': 4.0,
                },

                'hourglass': {
                    'centerX': 0.618,
                    'centerY': 0.00,
                    'axisLen': 0.017148277367054,
                },

                'lakes': {
                    'centerX': -0.339230468501458,
                    'centerY': 0.417970758224314,
                    'axisLen': 0.164938488846612,
                },

            }
        }

    def getFractal(self, name):
        if name in self.fractals['julia']:
            return "julia"
        elif name in self.fractals['mandlebrot']:
            return "mandlebrot"

    def getImageType(self, name, fractal):
        for image in self.fractals[fractal]:
            if name == image:
                return image

    def getImageInformation(self, info, fractal, image):

        return self.fractals[fractal][image][info]

    def getListOfFractalImages(self):
        myList = []
        for i in self.fractals:
            for j in self.fractals[i]:
                myList.append(j)
        return myList

