import pyglet
import os
from pathlib import Path
from pipeline_factory import *
import numpy as np
import OpenGL.GL as GL
import sys
sys.path.insert(0,"C:/Users/kickk/OneDrive/Documentos/GitHub/car_pyglet")
from modules.transforms import *
path = Path(os.path.dirname(os.path.dirname(__file__)))
with open(path / "shaders/transform_vertex.glsl") as f:
    vertex_source_code = f.read()
with open(path / "shaders/basic_fragment.glsl") as f:
    fragment_source_code = f.read()
window = pyglet.window.Window(720,480)
pipeline = Pipeline(vertex_source_code,fragment_source_code)

if __name__ == "__main__":
    position_data = np.array([-0.5, -0.5, 0.0, 
                               0.0,  0.5, 0.0, 
                               0.5, -0.5, 0.0],dtype=np.float32)
    color_data = np.array([1.0, 0.0, 0.0,
                        0.0, 1.0, 0.0,
                        0.0, 0.0, 1.0],dtype=np.float32)
    index_data = np.array([0,1,2])

    gpu_triangle = pipeline.vertex_list_indexed(len(position_data)//3,GL.GL_TRIANGLES,index_data)
    gpu_triangle.position[:] = position_data
    gpu_triangle.color[:] = color_data
    @window.event
    def on_draw():
        GL.glClearColor(0.0,0.0,0.0,1.0)
        pipeline.use()
        gpu_triangle.draw(GL.GL_TRIANGLES)

    @window.event 
    def on_key_press(symbol,modifiers):
        if (pyglet.window.key.LEFT == symbol):
            print("Izquierda")
    pyglet.app.run()