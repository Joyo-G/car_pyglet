import pyglet
import os
import numpy as np
import OpenGL.GL as GL
from pathlib import Path
#####################################################
#             IMPORTAR LOS SHADERS
#####################################################
path = Path(os.path.dirname(os.path.dirname(__file__)))
with open(path / "shaders/basic_vertex.glsl") as v:
    vertex_source_code = v.read()
with open(path / "shaders/basic_fragment.glsl") as f:
    fragment_source_code = f.read()

#####################################################
#         Creación de las Clases Pipeline y Model
#####################################################
class Pipeline(pyglet.graphics.shader.ShaderProgram):

    def __init__(self,vertex_souce, fragment_source):
        self.__vertex = pyglet.graphics.shader.Shader(vertex_souce,"vertex")
        self.__fragment = pyglet.graphics.shader.Shader(fragment_source,"fragment")
        super().__init__(self.__vertex,self.__fragment)

class Model:
    def __init__(self):
        self._position_data = None
        self._index_data = None
        self._color_data = None
        self._gpu_data = None
    
    def build(self,pipeline):
        self._gpu_data = pipeline.vertex_list_indexed(len(self._position_data)//3,GL.GL_TRIANGLES,self._index_data)
        self._gpu_data.position[:] = self._position_data
        self._gpu_data.color[:] = self._color_data
    
    def draw(self,mode=GL.GL_TRIANGLES):
        self._gpu_data.draw(mode)

#####################################################
#         Creación de las Clase Circle
#####################################################
class Circle(Model):
    def __init__(self,N=6,radio=1.0):
        self.__n = N
        self.__color_center = [1.0,1.0,1.0]
        self.__color_perimeter = [1.0,1.0,1.0]
        self.__radio = radio
        super().__init__()
        
    def setCenterColor(self,R,G,B):
        self.__color_center[0] = R
        self.__color_center[1] = G
        self.__color_center[2] = B
    def setPerimeterColor(self,R,G,B):
        self.__color_perimeter[0] = R
        self.__color_perimeter[1] = G
        self.__color_perimeter[2] = B
    
    def __makeVertexData(self):
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
        self.__makeVertexData()
        super().build(pipeline)

#####################################################
#   Creación de la ventana y la figura del circulo
#####################################################
pipeline = Pipeline(vertex_source_code, fragment_source_code)

window = pyglet.window.Window(600,600)

if __name__ == "__main__":
    
    gpu_circle = Circle(N=100,radio=0.3)
    gpu_circle.setPerimeterColor(1.0,0.0,0.0)
    gpu_circle.build(pipeline)
    @window.event
    def on_draw():
        GL.glClearColor(0, 0, 0, 1.0) #color de fondo
        pipeline.use()
        gpu_circle.draw(GL.GL_TRIANGLES)
    pyglet.app.run()

