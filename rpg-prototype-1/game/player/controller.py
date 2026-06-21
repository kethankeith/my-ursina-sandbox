from ursina import *

preset = {
        'preset1': color.green,
        'preset2': color.red
        }

class Player:
    def __init__(self, state, spawnpoint):
        self.state = state
        self.object = state.addEntity(
                name='player',
                model='quad',
                color=color.green,
                position=spawnpoint,
                scale=0.3
                )
