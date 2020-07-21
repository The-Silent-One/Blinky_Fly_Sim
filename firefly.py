from graphics import *
from time import sleep
from random import randint
from traffic import *

freq = 1
gray = "#87857e"
yellow = "#b9f043"
t_snooze = 3

class FireFly:
    
    def __init__(self,win,pop,factor,grid_size):
        
        self.size = int( grid_size / 5 )
        x , y = 0 , 0
        
        while [x,y] in pop:
            x = randint( 1, factor-1 )
            y = randint( 1, factor-1 )
        
        pop.append([x,y])
        
        self.gridx = x
        self.gridy = y
        
        ### grid box
        ### b0-b1
        ### |  |
        ### b3-b2
        
        b0 = Point(self.gridx*grid_size,self.gridy*grid_size)
        b2 = Point((self.gridx+1)*grid_size,(self.gridy+1)*grid_size)
        
        box = Rectangle( b0 , b2 )
        box.draw(win)
        
        self.posx = int( b0.getX() + grid_size / 2)
        self.posy = int( b0.getY() + grid_size / 2)
        
        self.head = Circle(Point(self.posx,self.posy-self.size),self.size)
        
        self.abdo = Oval(Point(self.posx-self.size, self.posy-self.size),Point(self.posx+self.size, self.posy+2*self.size))
        
        self.wing = Polygon(Point(self.posx-2*self.size ,self.posy-self.size),Point(self.posx++2*self.size,self.posy-self.size),Point( self.posx,self.posy+3*self.size/2))
        
        self.wing.draw(win)
        self.head.draw(win)
        self.abdo.draw(win)
        
        self.head.setFill(gray)
        self.abdo.setFill(gray)
        self.wing.setFill(gray)
        
        self.head.setOutline(gray)
        self.abdo.setOutline(gray)
        self.wing.setOutline(gray)
        
        self.coord = [self.gridx,self.gridy]
        self.broadcast = Thread(target=self.flyWriter,args=(in_q,out_q))
        
        self.broadcast.start()
        self.draw_q = Queue()
        self.flash()
        
    def flash(self):
        try:
            while True:
                data = self.draw_q.get_nowait()
                print(data)
                if data:
                    self.abdo.setFill(yellow)
                    sleep(freq)
                    self.abdo.setFill(gray)
        except Exception as e:
            #print(e)
            pass
    
    def flyWriter(self,in_q,out_q):
        in_q.put(self.coord)
        sleep(t_snooze)
        print("up")
        while True:
            while(not(isItMe(out_q,self.coord,freq))) :
                x = randint( 1, 100 )
                if x <= p:
                    print("random")
                    in_q.put(str(self.coord))
                    self.draw_q.put("f")
                else:
                    sleep(freq)
            
            #print([str(coord)])
            in_q.put(str(self.coord))
            self.draw_q.put("f")
            sleep(freq)

