import pyglet
import OpenGL.GL as GL
class Model:
    """
    This class is to controll all model data of shape.

    :version 1.0.1
    """
    def __init__(self):
        """
        Initializer a Model class with a position, index, color, and gpu data with None default value
        """
        self._position_data = None
        self._index_data = None
        self._color_data = None
        self._gpu_data = None
        self.pipeline = None
    def build(self,pipeline):
        """
        Initializer the gpu data attribute with and buffer, setting the position and color of the shape.
        """
        self.pipeline = pipeline
        self._gpu_data = pipeline.vertex_list_indexed(len(self._position_data)//3,GL.GL_TRIANGLES,self._index_data)
        self._gpu_data.position[:] = self._position_data
        self._gpu_data.color[:] = self._color_data
    
    def draw(self,mode=GL.GL_TRIANGLES):
        """
        Draw the shape with the specified mode (GL_TRIANGLES by default)
        """
        self._gpu_data.draw(mode)