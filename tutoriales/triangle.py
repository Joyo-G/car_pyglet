import pyglet
import numpy as np
import OpenGL.GL as GL
from pipeline_factory import *
#Traemos la función para crear el Pipeline
from lectura_de_shaders import *
#Traemos los vertex_source_code y fragment_source_code

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