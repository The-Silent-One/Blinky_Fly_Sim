class StoppableThread:
    def __init__(self): 
        self._running = True
      
    def terminate(self): 
        self._running = False
