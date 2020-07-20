from queue import Queue
from threading import Thread
from time import sleep , time
from operator import itemgetter
from random import randint

q = Queue()
p = 10

def dist(fly1,fly2):
    #print(fly1)
    #print(fly2)
    return (fly1[0] - fly2[0])**2+(fly1[1]-fly2[1])**2

def nearestNeighbor(fly,grid):
    neigh = [ [f,dist(fly,f)] for f in grid ]
    neigh = sorted(neigh,key=lambda k:k[1])[1:]
    #print(neigh)
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
    for n in neighs[data[0]]:
        queue.put([n,data[1]])
        
def tunnel(queue,nb_pop):
    grid = collectFlies(queue,nb_pop)
    #print(grid)
    neighs = dict()
    for fly in grid :
        neighs[str(fly)]=nearestNeighbor(fly,grid)
    #print(neighs)
    while True:
        data = queue.get()
        queue.task_done()
        print(data)
        broadcast(queue,data,neighs)
        #print(neighs[data[0]])
        
def flyWriter(queue,coord,freq,t_gap):
    queue.put(coord)
    sleep(t_gap)
    print("up")
    while True:
        while(not(isItMe(queue,coord,freq))) :
            x = randint( 1, 100 )
            if x <= p:
                print("random")
                queue.put([str(coord),"ping"])
            else:
                sleep(freq)
        
        #print([str(coord),data])
        queue.put([str(coord),"pong"])
        sleep(freq)

def isItMe(queue,coord,freq):
    if queue.empty():
        return False
    data = queue.get()
    queue.task_done()
    #print(data)
    if data[0]==coord:
        print("me")
        return True
    else:
        queue.put(data)
        return False
        
t1 = Thread(target=flyWriter,args=(q,[1,2],2,3))
t2 = Thread(target=flyWriter,args=(q,[3,4],2,3))
t3 = Thread(target=tunnel,args=(q,2))

t1.start()
t2.start()
t3.start()

#nearestNeighbor([1,1],[[1,1],[1,2],[2,1],[5,4],[3,1]])
