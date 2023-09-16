import numpy as np

class ModelController():
    """
    Create a controller for model transformations
    """
    def __init__(self):
        """
        Initialize the position in the origin, scale equals to 1 and without rotation
        """
        self.position = np.array([0,0,0],dtype=np.float32)
        self.scale = np.array([1,1,1],dtype=np.float32)
        self.rotate = np.array([0,0,0],dtype=np.float32)
