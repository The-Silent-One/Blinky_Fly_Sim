from graphics import *
from time import sleep
from firefly import *
import threading

window_size = 500
name = "Firefly map"

factor = 20
grid_size = window_size / factor
list_class_threads = list()

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
    win.close()
    for t in list_class_threads:
        t.terminate()
    for t in threading.enumerate()[1:]:
        t.join()
    sys.exit()
    
win = build(name,window_size)
pop = [[0,0]]
fly_pop = list()

for i in range(2):
    fly_pop.append(FireFly(win,pop,factor,grid_size,list_class_threads))
print(pop)

tun = Tunnel()
t = Thread(target=tun.run,args=(in_q,out_q,draw_q,2))
t.start()
list_class_threads.append(tun)
try:
    while True:
        while draw_q.empty():
            pass
        data = draw_q.get_nowait()
        print("data {}".format(data))
        flashThis(data,fly_pop)
except (KeyboardInterrupt,SystemExit):
    print("Stopped")
    kill(win)
