from queue import Queue
from threading import Thread
from time import sleep , time
from operator import itemgetter
from random import randint
from stoppableThread import *

in_q = Queue()
out_q = Queue()
draw_q = Queue()
p = 10

def dist(fly1,fly2):
    #print(fly1)
    #print(fly2)
    return (fly1[0] - fly2[0])**2+(fly1[1]-fly2[1])**2

def nearestNeighbor(fly,grid):
    neigh = [ [f,dist(fly,f)] for f in grid ]
    neigh = sorted(neigh,key=lambda k:k[1])[1:]
    #print(neigh)
    if not(len(neigh)):
        print("lonely")
        return list()
    
    val = neigh[0][1]
    res = list()
    for elt in neigh:
        if (elt[1]==val):
            res.append(str(elt[0]))
    #print(res)
    return res
    
def collectFlies(queue,nb_pop):
    grid = list()
    for i in range(nb_pop):
        data = queue.get()
        queue.task_done()
        #print(data)
        if (type(data)==type(list()) and len(data)==2 and type(data[0])==type(1)):
            grid.append(data)
    return grid

def broadcast(queue,data,neighs):
    for n in neighs[data]:
        #print("neighbor : {}".format(n))
        queue.put(n)
       
class Tunnel(StoppableThread):
    def run(self,in_q,out_q,draw_q,nb_pop):
        grid = collectFlies(in_q,nb_pop)
        #print(grid)
        neighs = dict()
        for fly in grid :
            neighs[str(fly)]=nearestNeighbor(fly,grid)
        #print(neighs)
        while self._running:
            data = in_q.get()
            in_q.task_done()
            #print(data)
            broadcast(draw_q,data,neighs)
            #print(neighs[data[0]])

def isItMe(queue,coord,freq):
        if queue.empty():
            return False
        data = queue.get()
        queue.task_done()
        #print(data)
        if data==str(coord):
            #print("me")
            return True
        else:
            queue.put(data)
            return False
        
#test()
