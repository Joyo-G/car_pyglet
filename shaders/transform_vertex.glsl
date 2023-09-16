#version 330

in vec3 position;
uniform mat4 transform = mat4(1.0);
in vec3 color;

out vec3 fragColor;

void main(){
    fragColor = color;
    gl_Position = transform * vec4(position,1.0f);
}