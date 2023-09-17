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

def uniformScale(s_u):
    return np.array([[s_u,0.0,0.0,0.0],
                     [0.0,s_u,0.0,0.0],
                     [0.0,0.0,s_u,0.0],
                     [0.0,0.0,0.0,1.0]], dtype = np.float32)

def uniformScale(s_x,s_y,s_z):
    return np.array([[s_x,0.0,0.0,0.0],
                     [0.0,s_y,0.0,0.0],
                     [0.0,0.0,s_z,0.0],
                     [0.0,0.0,0.0,1.0]], dtype = np.float32)

def rotateZ(theta):
    sin_theta = np.sin(theta)
    cos_theta = np.cos(theta)
    return np.array([
        [cos_theta,-sin_theta,0,0],
        [sin_theta,cos_theta,0,0],
        [0,0,1,0],
        [0,0,0,1]], dtype = np.float32)

def rotateX(theta):
    sin_theta = np.sin(theta)
    cos_theta = np.cos(theta)
    return np.array([
        [1,0,0,0],
        [0,cos_theta,-sin_theta,0],
        [0,sin_theta,cos_theta,0],
        [0,0,0,1]], dtype = np.float32)

def rotateY(theta):
    sin_theta = np.sin(theta)
    cos_theta = np.cos(theta)
    return np.array([
        [cos_theta,0,sin_theta,0],
        [0,1,0,0],
        [-sin_theta,0,cos_theta,0],
        [0,0,0,1]], dtype = np.float32)