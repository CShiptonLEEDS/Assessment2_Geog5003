# -*- coding: utf-8 -*-
"""
Show me the way to go home...
"""

import random

# Set the agents, assing a house number, set their path home

class Drunk():
    def __init__(self, environment, drunk, house):
        # Set the location of the pub
        self.x = 100
        self.y = 110
        self.environment = environment
        self.drunk = drunk
        self.house = house
        self.home = False  
        

    #Move the agents
    #randomising the movement
    #to come back through down or left respectively
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % len(self.environment) 
        else:
            self.y = (self.y - 1) % len(self.environment)
        
        if random.random() < 0.5:
            self.x = (self.x + 1) % len(self.environment)
        else:
            self.x = (self.x - 1) % len(self.environment)
