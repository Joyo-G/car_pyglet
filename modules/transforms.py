import numpy as np

def indentidy():
    return np.array([[1.0,0.0,0.0,0.0],
                     [0.0,1.0,0.0,0.0],
                     [0.0,0.0,1.0,0.0],
                     [0.0,0.0,0.0,1.0]], dtype = np.float32)

def translate(dx,dy,dz):
    return np.array([[1.0,0.0,0.0,dx],
                     [0.0,1.0,0.0,dy],
                     [0.0,0.0,1.0,dz],
                     [0.0,0.0,0.0,1.0]], dtype = np.float32)