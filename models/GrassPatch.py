from itertools import count
from mesa import Agent 

class GrassPatch(Agent):

    def __init__(self,id,position,model,fully_grow,countdown):
        """
        Creates a new patch of grass
        @params
            grown: (boolean) Whether the patch of grass is fully grown or not
            countdown: Time for the patch of grass to be fully grown again
        """
        super().__init__(id,model)
        self.position = position
        self.fully_grown = fully_grow
        self.countdown = countdown

    def step(self):
        if not self.fully_grown:
            if self.countdown <= 0:
                self.fully_grown = True 
                self.countdown = self.model.grass_regrowth_time
            else:
                self.countdown -= 1