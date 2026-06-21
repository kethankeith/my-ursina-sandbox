import builtins
from ursina import *

from ursina import vec3
from ursina import shader
from ursina.color import rgba32
from ursina.shaders import lit_with_shadows_shader

zoom_level = 5

#camera settings
def default_camera_settings():
    camera.orthographic = True
    camera.fov = zoom_level

def global_new():
    default_camera_settings()
    #default level ^

def global_update():
    camera.fov = zoom_level
    #default level ^

def global_input(key):
    if key == 'g':
        print("Hello")


##State class

def _default_new(self):
    Light = PointLight(y=10)
    Light.color = color.white

    room = self.Entity(model='temp_room.obj', color=color.gray, z=-5)
    cube = self.Entity(model='cube', name='cube', color=color.orange, z=-9, y=-1.7)

    #EditorCamera()

class state:
    classnum = 0

    def _collectEnt(self, instanced_ent, name, parent):
        self.workspace[name] = instanced_ent
        if not parent:
            instanced_ent.parent_setter(self.instance)

        if parent == camera.ui:
            self.ui[name] = instanced_ent
        else:
            self.collection.insert(0, instanced_ent)

    def Entity(self, **kwargs):
        name = kwargs.pop('name', f"entity{len(self.workspace)}")
        parent = kwargs.get('parent', None)

        ent = Entity(**kwargs)
        self._collectEnt(ent, name, parent)

        return ent

    def Text(self, **kwargs):
        name = kwargs.pop('name', f"entity{len(self.workspace)}")
        parent = kwargs.get('parent', camera.ui)

        ent = Text(**kwargs)
        self._collectEnt(ent, name, parent)

        return ent


    def __init__(self, **kwargs):
        self.name = kwargs.pop('name', f"classno{state.classnum}")
        new = kwargs.pop('new', _default_new)
        update = kwargs.pop('update')
        input = kwargs.pop('input')

        def wrapped_new(manager):
            global_new()

            self.instance = Entity(model='quad', color=color.rgba32(0, 0, 0, 0))
            self.manager = manager

            camera.rotation = Vec3(0, 0, 0)
            camera.position = Vec3(0, 0, -20) #for some reason -20 is the origin
            camera.orthographic = False
            camera.fov = 40

            new(self)

        def wrapped_update():
            global_update()
            update(self)

        def wrapped_input(key):
            global_input(key)
            input(self, key)

        self.input = wrapped_input
        self.new = wrapped_new
        self.update = wrapped_update

        self.workspace = {}
        self.collection = []
        self.ui = {}

        for key, value in kwargs.items():
            setattr(self, key, value)

        state.classnum += 1

    def clean(self):
        for key in self.ui:
            destroy(self.ui[key])

        for ent in self.collection:
            if isinstance(ent, (DirectionalLight, AmbientLight, PointLight)):
                ent.remove_node()
            else:
                destroy(ent)

        self.workspace = {}
        self.ui = {}

##State Manager
class stateman:
    def __init__(self):
        self.state_rep = {}
        self.current_state = None

    def add_state(self, state):
        self.state_rep[state.name] = state

    def change_state(self, nxt_state):
        if self.current_state:
            builtins.render.clear_light()
            destroy(self.current_state.instance)

            if hasattr(self.current_state, 'clean'):
                self.current_state.clean()

        if nxt_state.name in self.state_rep:
            self.current_state = nxt_state

            self.current_state.new(self)
        else:
            print(f"Error: State '{nxt_state}'")

    def update(self):
        if self.current_state:
            self.current_state.update()

    def input(self, key):
        if self.current_state:
            self.current_state.input(key)
