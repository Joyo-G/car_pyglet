import pyglet
#La clase Window tiene los siguientes parámetros
#Window(width=None, height=None, caption=None, resizable=False, 
#       style=None, fullscreen=False, visible=True, vsync=True, 
#       file_drops=False, display=None, screen=None, config=None, 
#       context=None, mode=None)
window = pyglet.window.Window(600,600)
@window.event 
def on_draw():
    #Esta función se ejecuta en ciclo
    pass
pyglet.app.run()