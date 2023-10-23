
from shapes.model import Model


class Cube(Model):

    def __init__(self):
        super().__init__()
        self.__loadPositionData()
        self.__loadVertexData()
    def __loadPositionData(self):
        # Defining the location and colors of each vertex  of the shape
        self._position_data = [
        #   positions       
        # Z+
            -0.5, -0.5,  0.5,
            0.5, -0.5,  0.5,
            0.5,  0.5,  0.5, 
            -0.5,  0.5,  0.5,

        # Z-
            -0.5, -0.5, -0.5, 
            0.5, -0.5, -0.5, 
            0.5,  0.5, -0.5, 
            -0.5,  0.5, -0.5, 
            
        # X+
            0.5, -0.5, -0.5,
            0.5,  0.5, -0.5,
            0.5,  0.5,  0.5,
            0.5, -0.5,  0.5,
    
        # X-
            -0.5, -0.5, -0.5, 
            -0.5,  0.5, -0.5, 
            -0.5,  0.5,  0.5, 
            -0.5, -0.5,  0.5, 

        # Y+
            -0.5, 0.5, -0.5,
            0.5, 0.5, -0.5,
            0.5, 0.5,  0.5,
            -0.5, 0.5,  0.5,

        # Y-
            -0.5, -0.5, -0.5, 
            0.5, -0.5, -0.5, 
            0.5, -0.5,  0.5, 
            -0.5, -0.5,  0.5,
            ]

    def __loadVertexData(self):
        # Defining connections among vertices
        # We have a triangle every 3 indices specified
        self._index_data = [
            0, 1, 2, 2, 3, 0, # Z+
            7, 6, 5, 5, 4, 7, # Z-
            8, 9,10,10,11, 8, # X+
            15,14,13,13,12,15, # X-
            19,18,17,17,16,19, # Y+
            20,21,22,22,23,20] # Y-

    def setColor(self,r,g,b):
        self._color_data = [r,g,b]*24

print([0.1,0.1,0.1]*3)