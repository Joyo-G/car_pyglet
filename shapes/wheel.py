import pyglet
from model import Model
import numpy as np
class Wheel(Model):

    def __init__(self,N,color_goma = [0.0,0.0,0.0],color_metal = [1.0,1.0,1.0]):
        super().__init__()
        self.__color_goma = color_goma
        self.__n = N
        self.__color_metal = color_metal

    def __makeWheel(self):
        #Metal parte de atras y adelante
        position_data = [0.0, 0.0, 0.0]
        index_data = []
        color_data = []
        color_data+=self.__color_metal
        alpha = 2*np.pi/(self.__n)
        for i in range(self.__n):
            delta = alpha*i
            position_data+=[np.cos(delta)*0.5, np.sin(delta)*0.5, 0.0 ]
            index_data += [0, i,(i+1)]
            color_data += self.__color_metal
        index_data+=[0, self.__n, 1]
        self._position_data = np.array(position_data)
        self._color_data = np.array(color_data)
        self._index_data = np.array(index_data)