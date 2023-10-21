import pyglet
import numpy as np
class Pipeline(pyglet.graphics.shader.ShaderProgram):
    """
    Create and ShaderProgram with the vertex and fragment source
    """
    def __init__(self,vertex_souce, fragment_source):
        """
        Initialize an ShaderProgram with the vertex and fragment source as shader
        """
        self.__vertex = pyglet.graphics.shader.Shader(vertex_souce,"vertex")
        self.__fragment = pyglet.graphics.shader.Shader(fragment_source,"fragment")
        super().__init__(self.__vertex,self.__fragment)

    def set_uniform(self,uniform_name,value,type):
        if self[uniform_name] is None:
            raise Exception("Uniform value does not exist")
        if type == "matrix4":
            self[uniform_name] = np.reshape(value,(16,1),"F")
