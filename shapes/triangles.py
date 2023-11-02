import numpy as np
import os
import sys
sys.path.append(os.path.dirname(__file__))
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

    

    