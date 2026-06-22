from ursina import *

preset = {
        'preset1': color.green,
        'preset2': color.red
        }

grid_size = 0.4 #later to be given by a world variable

class Mov_mngr:
    def __init__(self, plr):
        self.plr = plr
        self.state = plr.state

        self.dir = Vec2()
        self.speed = 0.2

        tracker = {}
        def button():
            value = 1

        self.state.addBinds({
            'left arrow' : lambda s: self.walkdirection(Vec2(-1, 0)),
            'left arrow up' : lambda s: self.walkdirection(Vec2()),
            'right arrow' : lambda s: self.walkdirection(Vec2(1, 0)),
            'right arrow up' : lambda s: self.walkdirection(Vec2()),
            'up arrow' : lambda s: self.walkdirection(Vec2(0, 1)),
            'up arrow up' : lambda s: self.walkdirection(Vec2()),
            'down arrow' : lambda s: self.walkdirection(Vec2(0, -1)),
            'down arrow up' : lambda s: self.walkdirection(Vec2())
                })

    def queue(self, time):
        value = 1

    def walkdirection(self, direction):
        self.dir = direction
        self.queue(self.speed)
        print(self.dir)

class Player:
    def __init__(self, state, spawnpoint):
        self.state = state
        self.char = state.addEntity(
                name='player',
                model='quad',
                color=color.green,
                position=spawnpoint,
                scale=0.3,
                #update=lambda: print("hello")
                )
        self.mov = Mov_mngr(self)

