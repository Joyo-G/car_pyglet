import numpy as np
from model import Model

class Triangle(Model):
    """
    Create a Triangle Model with the vertices A,B,C.
    """
    def __init__(self):
        """
        Initialize the Triangle Model with the color and vertices default values.
        """
        super().__init__()
        self._position_data = np.array([-0.5, -0.5, 0.0, 
                                    0.0,  0.5, 0.0, 
                                    0.5, -0.5, 0.0],dtype=np.float32)
        self._color_data = np.array([1.0, 0.0, 0.0,
                                0.0, 1.0, 0.0,
                                0.0, 0.0, 1.0],dtype=np.float32)
        self._index_data = np.array([0,1,2],dtype=np.int32)
    
    def setVertex(self,W,x,y,z):
        """
        Set the vertex W with values (x,y,z)
        """
        if W == "A":
            self._position_data[:3] = [x,y,z]
        elif W == "C":
            self._position_data[3:6] = [x,y,z]
        elif W == "B":
            self._position_data[6:] = [x,y,z]
        else:
            raise Exception("W must be A, B or C")
    def setColorVertex(self,W,r,g,b):
        """
        Set vertex W color with values (r,g,b)
        """
        if W == "A":
            self._color_data[:3] = [r,g,b]
        elif W == "C":
            self._color_data[3:6] = [r,g,b]
        elif W == "B":
            self._color_data[6:] = [r,g,b]
        else:
            raise Exception("W must be A, B or C")

    

    