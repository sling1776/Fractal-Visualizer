
class Gradient:
    """
    This is the Gradient Class. Essentially it is just a list of different colors. In the
    future it will be easy to write in a calculation function to get even more colors than
    these few.
    """
    def __init__(self, number):
        raise NotImplementedError("Concrete subclass of Gradient must implement __init__")

    def getColor(self, iterations):
        raise NotImplementedError("Concrete subclass of Gradient must implement getColor() method")

