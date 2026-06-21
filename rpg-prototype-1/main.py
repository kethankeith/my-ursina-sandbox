## Reminder to myself:
## main.py is only meant for four things, noted by the four letters IWIS
## (I)nitialize the framework
## (W)indow configuration
## (I)nstantiate the state manager
## (S)tart the game loop

from ursina import *
from game.engine import stateman
from game.level1 import level1

levels = [level1]

app = Ursina()

engine = stateman()
for l in levels:
    engine.add_state(l)

engine.change_state(level1)

window.forced_aspect_ratio = 16/9
window.size = (1280, 720)
window.borderless = False


def input(key): 
    engine.input(key)
    max_lvl = len(levels)
    current = levels.index(engine.current_state) + 1

    if key == 'left arrow':
        current = (current % max_lvl)
        engine.change_state(levels[current])
    if key == 'right arrow':
        current = ((current - 2) % max_lvl)
        engine.change_state(levels[current])

def update():
    engine.update()

app.run()
