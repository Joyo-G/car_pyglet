import pyglet
import OpenGL.GL as GL
from pathlib import Path
import os
import sys
import time
import numpy as np

WIDTH = 720
HEIGHT = 480

path = Path(os.path.dirname(os.path.dirname(__file__)))
with open(path / "shaders/transform_vertex.glsl") as v:
    vertex_source_code = v.read()
with open(path / "shaders/basic_fragment.glsl") as f:
    fragment_source_code = f.read()

class Pipeline(pyglet.graphics.shader.ShaderProgram):
    def __init__(self,vertex_souce, fragment_source):
        self.__vertex = pyglet.graphics.shader.Shader(vertex_souce,"vertex")
        self.__fragment = pyglet.graphics.shader.Shader(fragment_source,"fragment")
        super().__init__(self.__vertex,self.__fragment)

    def set_uniform(self,uniform_name,value,type):
        if self[uniform_name] is None:
            raise Exception("Uniform value does not exist")
        elif type == "matrix4":
            self[uniform_name] = np.reshape(value,(16,1),"F")
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
class ModelController():

    def __init__(self):
        self.position = np.array([0,0,0],dtype=np.float32)
        self.scale = 1
        self.rotate = np.array([0,0,0],dtype=np.float32)
class Triangle(Model):

    def __init__(self):
        super().__init__()
        self._position_data = np.array([-0.5, -0.5, 0.0, 
                                    0.0,  0.5, 0.0, 
                                    0.5, -0.5, 0.0],dtype=np.float32)
        self._color_data = np.array([1.0, 0.0, 0.0,
                                0.0, 1.0, 0.0,
                                0.0, 0.0, 1.0],dtype=np.float32)
        self._index_data = np.array([0,1,2],dtype=np.int32)
    
    def setVertex(self,W,x,y,z):
        if W == "A":
            self._position_data[:3] = [x,y,z]
        elif W == "C":
            self._position_data[3:6] = [x,y,z]
        elif W == "B":
            self._position_data[6:] = [x,y,z]
        else:
            raise Exception("W must be A, B or C")
    def setColorVertex(self,W,r,g,b):
        if W == "A":
            self._color_data[:3] = [r,g,b]
        elif W == "C":
            self._color_data[3:6] = [r,g,b]
        elif W == "B":
            self._color_data[6:] = [r,g,b]
        else:
            raise Exception("W must be A, B or C")
class ModelTransform(ModelController):

    def __init__(self):
        super().__init__()
    
    def getTransformation(self):
        return translate(self.position[0],self.position[1],self.position[2]) @ uniformScale(self.scale)
def translate(dx,dy,dz):
    return np.array([[1.0,0.0,0.0,dx],
                     [0.0,1.0,0.0,dy],
                     [0.0,0.0,1.0,dz],
                     [0.0,0.0,0.0,1.0]], dtype = np.float32)
def uniformScale(s_u):
    return np.array([[s_u,0.0,0.0,0.0],
                     [0.0,s_u,0.0,0.0],
                     [0.0,0.0,s_u,0.0],
                     [0.0,0.0,0.0,1.0]], dtype = np.float32)
if __name__ == "__main__":

    window = pyglet.window.Window(width = WIDTH, height = HEIGHT,caption="Triangle moving")
    
    pipeline = Pipeline(vertex_source_code,fragment_source_code)
    triangle_gpu = Triangle()
    triangle_gpu.build(pipeline)
    triangle_controller = ModelTransform()
    GL.glClearColor(0.0,0.0,0.0,1.0)

    @window.event 
    def on_draw():
        window.clear()
        pipeline.use()
        pipeline.set_uniform("u_transform",triangle_controller.getTransformation(),"matrix4")
        triangle_gpu.draw()

    @window.event 
    def on_key_press(symbol,modifies):
        if (pyglet.window.key.LEFT == symbol):
            triangle_controller.position[0]-=0.1
        if (pyglet.window.key.RIGHT == symbol):
            triangle_controller.position[0]+=0.1
        if (pyglet.window.key.UP == symbol):
            triangle_controller.position[1]+=0.1
        if (pyglet.window.key.DOWN == symbol):
            triangle_controller.position[1]-=0.1
        if (pyglet.window.key.PLUS == symbol):
            triangle_controller.scale+=0.1
        if (pyglet.window.key.MINUS == symbol):
            triangle_controller.scale-=0.1
    pyglet.app.run()
