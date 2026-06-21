from ursina import *
from game.engine import state
from game.player import Player

def on_new_scene(self):
    plr = Player(self, Vec3(-0.3, 0, 0))
    quadc = self.addEntity(
                        name='quadtocompare',
                        model='quad',
                        position=(0.3, 0, 1))

def scene_on_update(self):
    value = 1

def left_pressed(state):
    print("Left Arrow Pressed")

scene_bindings = {
        'left arrow': left_pressed
        }

level1 = state(
        name = "level1",
        update=scene_on_update,
        new=on_new_scene,
        bindings=scene_bindings,
        )
