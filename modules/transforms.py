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

def scale(s_x,s_y,s_z):
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

def lookAt(eye, at, up):

    forward = (at - eye)
    forward = forward / np.linalg.norm(forward)

    side = np.cross(forward, up)
    side = side / np.linalg.norm(side)

    newUp = np.cross(side, forward)
    newUp = newUp / np.linalg.norm(newUp)

    return np.array([
            [side[0],       side[1],    side[2], -np.dot(side, eye)],
            [newUp[0],     newUp[1],   newUp[2], -np.dot(newUp, eye)],
            [-forward[0], -forward[1], -forward[2], np.dot(forward, eye)],
            [0,0,0,1]
        ], dtype = np.float32)

def ortho(left, right, bottom, top, near, far):
    r_l = right - left
    t_b = top - bottom
    f_n = far - near
    return np.array([
        [ 2 / r_l,0,0,-(right + left) / r_l],
        [ 0,2 / t_b,0,-(top + bottom) / t_b],
        [ 0,0,-2 / f_n,-(far + near) / f_n],
        [ 0,0,0,1]
        ], dtype = np.float32)

def frustum(left, right, bottom, top, near, far):
    r_l = right - left
    t_b = top - bottom
    f_n = far - near
    return np.array([
        [ 2 * near / r_l,
        0,
        (right + left) / r_l,
        0],
        [ 0,
        2 * near / t_b,
        (top + bottom) / t_b,
        0],
        [ 0,
        0,
        -(far + near) / f_n,
        -2 * near * far / f_n],
        [ 0,
        0,
        -1,
        0]], dtype = np.float32)


def perspective(fovy, aspect, near, far):
    halfHeight = np.tan(np.pi * fovy / 360) * near
    halfWidth = halfHeight * aspect
    return frustum(-halfWidth, halfWidth, -halfHeight, halfHeight, near, far)