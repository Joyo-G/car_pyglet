"""
This module implements an Scene Graph
"""

import networkx as nt
import numpy as np
from shapes.model import Model

__autor__ = "Gustavo Joyo"
__license__ = "MIT"
__version__ = "1.0.0"


class Leaf():

    def __init__(self):
        pass

    def draw(self):
        pass


class SceneNode():

    def __init__(self):
        pass

    def draw(self):
        pass

class SceneGraph():
    """
    Scene graph
    """
    def __init__(self):
        self.childs = []
        self.transform = tr.identidy()

    """
    Draw the scene graph
    """
    def draw(self):
        for node in self.childs:
            node.draw()

    def add_node(self,node):
        pass
    
    def getTransform(self):
        return self.transform

    def update(self):
        for node in self.childs:
            self.transform@=node.getTransform()



###Test

arbol = SceneGraph()

triangulo = Triangle()
triangulo.init_gpu_data()

cuadrado = Squad()
cuadrado.init_gpu_data()

arbol.add_node("hojas",transformation = ...)
arbol.add_node("tronco",cuadrado)


