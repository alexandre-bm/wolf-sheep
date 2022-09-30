from mesa import Agent
import numpy as np

class RandomWalker(Agent):

    grid = None
    x = None
    y = None
    moore = True

    def __init__(self,id,position,model,moore=True):
        """
        @params:
        - moore: if True, may move in all 8 directions
                 otherwise, only up, down, left or right
        """
        super().__init__(id,model)
        self.position = position
        self.moore = moore 

