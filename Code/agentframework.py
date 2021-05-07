# -*- coding: utf-8 -*-
"""
Created on Sun May  2 11:47:57 2021

@author: Eliza
"""

# Import required libraries.
import random

# Create "Agent" class.
class Agent():
    
    # Set up class constructor, to deal with the "environment" and "agents" lists.
    def __init__(self, environment, agents):
        self.y = random.randint(0,100)  # Assign y coordinate a random value between 0 and 100.
        self.x = random.randint(0,100)  # Assign x coordinate a random value between 0 and 100.
        self.environment = environment  # Save a link to the "environment" list within the class.
        self.agents = agents            # Save a link to the "agents" list within the class.
        self.store = 0                  # Create a variable to store how much the agents have 'eaten'.
        
        # Print agent list to ensure that each agent can see every other agent.
        # print(self.agents)
    
    # Create "move" function to move agents around the environment.
    def move(self):
        # If a random value between 0 and 1 is less than 0.5, move one position up on the environment.
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        # If a random value between 0 and 1 is greater than 0.5, move one position down on the environment.
        else:
            self.y = (self.y - 1) % 100
        # If a random value between 0 and 1 is less than 0.5, move one position forwards on the environment
        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        # If a random value between 0 and 1 is greater than 0.5, move one position backwards on the environment
        else:
            self.x = (self.x - 1) % 100
    
    # Create "eat" function to enable agents to deplete the environment.
    def eat(self):
        # If "environment" under "agent" has a value greater than 10, deplete it by 10, and add 10 to the agents store.
        if  self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
        # If "environment" under "agent" has a value less than 10, add the value to the agents store, then set to zero.
        else:
            self.store += self.environment[self.y][self.x]
            self.environment[self.y][self.x] = 0
                    
    # Create "share_with_neighbours" function to allow agents to share what is in their store.       
    def share_with_neighbours(self, neighbourhood):
        # Create a for-loop to loop through the agents.
        for agent in self.agents:
            dist = self.distance_between(agent) # Calculate distance between current agent and another.
            
            # If the distance between agents is less than the "neighbourhood" value, assign each agent an average of their stores.
            if dist <= neighbourhood:
                sum = self.store + agent.store
                ave = sum /2
                self.store = ave
                agent.store = ave
     
                # To test that "share_with_neighbours" and "distance_between" functions work, print the distance between two agents and their average store.
                # print("sharing " + str(dist) + " " + str(ave))
     
    # Create "distance_between" funciton to calculate the distance between the current agent and another.
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5 # Use pythagoras' theorem to calculate distance.


    # Had issues getting this working so made generic and commented it out.    
    ''' could implement a 'property' attribute like this
    def getx(self):
        return self._x
    
    def setx(self, VALUE):
        self._x = VALUE
        
    def delx(self):
        del self._x
        
    x = property(getx, setx, delx, "i'm the x property")
    '''
    

            
    
           
    