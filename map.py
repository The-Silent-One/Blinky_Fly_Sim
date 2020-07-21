from graphics import *
from time import sleep
from firefly import *

window_size = 500
name = "Firefly map"

factor = 20
grid_size = window_size / factor

def build(name,window_size):
    win = GraphWin(name,window_size,window_size)
    return win

        
def freeze(win):
    win.getMouse()
    win.close()
    
win = build(name,window_size)
pop = [[0,0]]
f = FireFly(win,pop,factor,grid_size)
print(pop)
sleep(2)
#f.flash()
#freeze(win)
