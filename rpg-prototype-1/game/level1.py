from ursina import *
from game.engine import state

def Player(self):
    lplr = self.Entity(
            name='player',
            model='quad',
            color=color.green,
            position=(-0.3, 0, 0),
            scale=0.3
            )
    
    return Player

def on_new_scene(self):
    plr = Player(self)
    quadc = self.Entity(
                        name='quadtocompare',
                        model='quad',
                        position=(0.3, 0, 1))

def scene_on_update(self):
    value = 1

def scene_input(self, key):
    if key == 'left arrow':
        print("Left Arrow Pressed")

level1 = state(
        name = "level1",
        update=scene_on_update,
        new=on_new_scene,
        input=scene_input,
        )
