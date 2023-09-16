import pyglet

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