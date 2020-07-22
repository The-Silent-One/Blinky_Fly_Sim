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

def getFly(coord,fly_pop):
    for f in fly_pop:
        if str(f.coord)==coord:
            return f
    return None

def flashThis(coord,fly_pop):
    f = getFly(coord,fly_pop)
    f.flash()
    
def kill(win):
    win.getMouse()
    win.close()
    
win = build(name,window_size)
pop = [[0,0]]
fly_pop = list()

for i in range(2):
    fly_pop.append(FireFly(win,pop,factor,grid_size))
print(pop)

while True:
    while draw_q.empty():
        pass
    data = draw_q.get_nowait()
    print("data {}".format(data))
    flashThis(data,fly_pop)
