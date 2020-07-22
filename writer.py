from time import sleep
from traffic import *
from stoppableThread import *

t_snooze = 3
freq = 1

class FlyWriter(StoppableThread):
    
    def run(self,fly,in_q,out_q,draw_q):
            in_q.put(fly.coord)
            sleep(t_snooze)
            print("up")
            while self._running:
                while(not(isItMe(out_q,fly.coord,freq)) and self._running) :
                    x = randint( 1, 100 )
                    if x <= p:
                        print("random")
                        draw_q.put(str(fly.coord))
                        in_q.put(str(fly.coord))
                        
                    else:
                        sleep(freq)
                
                #print([str(coord)])
                in_q.put(str(fly.coord))
                draw_q.put(str(fly.coord))
                sleep(freq)
