import os
from pathlib import Path

#__file__: Es la dirección del archivo actual
# os.path.dirname(__file__): Nos dice la dirección de donde se encuentra el archivo 
#                            (C:\Users\kickk\OneDrive\Documentos\GitHub\car_pyglet\tutoriales)
# Path se usa para poder usar el / y la ruta del archivo al que nos queremos dirigir.
# Ejemplo de uso:
#  ruta_base = Path("/ruta/base")
#  subruta = "subruta"
#  nueva_ruta = ruta_base / subruta
#  print(nueva_ruta)  # Esto imprimirá: /ruta/base/subruta
path = Path(os.path.dirname(os.path.dirname(__file__))) #Da la dirección de ../car_pyglet
with open(path / "shaders/basic_vertex.glsl") as v:
    #f.read() es nuestro código del archivo basic_vertex.glsl pasado a texto
    #Entonces lo almacenamos en una variable
    vertex_source_code = v.read()
#Lo mismo para el fragment
with open(path / "shaders/basic_fragment.glsl") as f:
    #f.read() es nuestro código del archivo basic_vertex.glsl pasado a texto
    #Entonces lo almacenamos en una variable
    fragment_source_code = f.read()


