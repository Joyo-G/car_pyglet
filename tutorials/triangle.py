import pyglet
import numpy as np
import OpenGL.GL as GL
from pathlib import Path
import os
#####################################################
#             IMPORTAR LOS SHADERS
#####################################################
path = Path(os.path.dirname(os.path.dirname(__file__)))
with open(path / "shaders/basic_vertex.glsl") as v:
    vertex_source_code = v.read()
with open(path / "shaders/basic_fragment.glsl") as f:
    fragment_source_code = f.read()

#####################################################
#             Creación de la clase Pipeline
#####################################################
class Pipeline(pyglet.graphics.shader.ShaderProgram):

    def __init__(self,vertex_souce, fragment_source):
        self.__vertex = pyglet.graphics.shader.Shader(vertex_souce,"vertex")
        self.__fragment = pyglet.graphics.shader.Shader(fragment_source,"fragment")
        super().__init__(self.__vertex,self.__fragment)

#Creamos el pipeline
pipeline = Pipeline(vertex_source_code, fragment_source_code)

window = pyglet.window.Window(600,600)

if __name__ == "__main__":
    #Imaginando que crearemos un triangulo con coordenadas en (-0.5,-0.5,0.0), (0.0,0.5,0.0) y (0.5,-0.5,0.0)
    position_data = np.array([-0.5, -0.5, 0.0, 
                               0.0,  0.5, 0.0, 
                               0.5, -0.5, 0.0],dtype=np.float32)
    #Usualmente la posición va al lado de los colores, pero en este caso los separaremos
    color_data = np.array([1.0, 0.0, 0.0,
                        0.0, 1.0, 0.0,
                        0.0, 0.0, 1.0],dtype=np.float32)
    index_data = np.array([0,1,2])

    gpu_triangle = pipeline.vertex_list_indexed(len(position_data)//3,GL.GL_TRIANGLES,index_data)
    gpu_triangle.position[:] = position_data
    gpu_triangle.color[:] = color_data

    @window.event
    def on_draw():
        GL.glClearColor(0, 0, 0, 1.0) #color de fondo
        pipeline.use()
        gpu_triangle.draw(GL.GL_TRIANGLES)
    pyglet.app.run()