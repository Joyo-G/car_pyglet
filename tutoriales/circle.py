import pyglet
import sys
sys.path.insert(0,"C:/Users/kickk/OneDrive/Documentos/GitHub/car_pyglet/shapes")
import os
import numpy as np
import OpenGL.GL as GL
from pipeline_factory import *
#Traemos la función para crear el Pipeline
from lectura_de_shaders import *
#Traemos los vertex_source_code y fragment_source_code
from circle import Circle


#Creamos el pipeline
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

