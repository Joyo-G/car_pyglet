import numpy as np
import pyglet
from shapes.model import Model
class Circle(Model):
    """ A circle with a N as amount of triangles and a radio.
    """
    def __init__(self,N=6,radio=1.0):
        """
        Initializer an circle with an N triangles and a radio.
        """
        self.__n = N
        self.__color_center = [1.0,1.0,1.0]
        self.__color_perimeter = [1.0,1.0,1.0]
        self.__radio = radio
        
    def setCenterColor(self,R,G,B):
        """
        Set the color of the center of the cicle
        """
        self.__color_center[0] = R
        self.__color_center[1] = G
        self.__color_center[2] = B
    def setPerimeterColor(self,R,G,B):
        """
        Set the color of the perimeter of the cicle
        """
        self.__color_perimeter[0] = R
        self.__color_perimeter[1] = G
        self.__color_perimeter[2] = B
    
    def __makeVertexData(self):
        """
        This makes the array of the vertex data of the circle
        """
        position_data = [0.0, 0.0, 0.0]
        index_data = []
        color_data = self.__color_center
        alpha = 2*np.pi/(self.__n)
        for i in range(self.__n):
            delta = alpha*i
            position_data+=[np.cos(delta)*self.__radio, np.sin(delta)*self.__radio, 0.0 ]
            index_data += [0, i,(i+1)]
            color_data += self.__color_perimeter
        index_data+=[0, self.__n, 1]
        self._position_data = np.array(position_data)
        self._color_data = np.array(color_data)
        self._index_data = np.array(index_data)
        
    def build(self,pipeline):
        """
        Build the circle in the gpu_data atribute
        """
        self.__makeVertexData()
        super().build(pipeline)