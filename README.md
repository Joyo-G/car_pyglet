# car_pyglet
This is a example of a car made in OpenGL, using Pyglet.

## Functions used in this repository (pyglet)
- pyglet.graphics.shader.Shader(source,type): Source can be text of the shader GLSL code. The kind is "vertex" or "fragment". This is used in Pipeline class. The function is used to save the source and the type to use them in the next function.
- pyglet.graphics.shader.ShaderProgram(vertex_shader,fragment_shader): This function recive that returns the before funtion. This function load the vertex and fragment shader source.
- pyglet.window.Window(): This function have many variables, this can be read in pyglet docs. This is used to create a window to project our primitives.
- **pipeline**.vertex_list_indexed(len(position_data)//3 ,GL.GL_TRIANGLES, index_data): After we have the vertex (position) data, and the indices data from our primite, we have to load them in this function, the return is saved in some variable gpu_name. After this, we must set position and color data, like this: "gpu_name.position[:] = position_data" and "gpu_name.color[:] = color_data". 
- gpu_name.draw(mode): This function is used to draw all data in gpu_name. The mode is the mode what we like to draw our primitive, usually GL.GL_TRIANGLES.

<video width="320" height="240" controls>
      <source src="/video.mp4" type="video/mp4">
      Your browser does not support the video tag.
    
</video>
