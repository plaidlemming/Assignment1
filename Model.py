# -*- coding: utf-8 -*-
"""
Created on Sun May  2 10:51:29 2021

@author: Eliza
"""

# Import required libraries.
import csv
import random
import matplotlib.pyplot
import agentframework
import matplotlib.animation 

# Create parameters for ABM.
num_of_agents = 10      # Create variable and assign it a number of agents.
num_of_iterations = 100  # Create variable and assign it a number of iterations of the model.
neighbourhood = 20      # Create variable and assign it a value determining 'nearby' agents.

# Create agent and environment variables.
agents = []
environment = []

# Open 'in.txt' file and save as variable "f".
f = open('in.txt', newline='')
# Parse "f" and save to "reader" variable.
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

# Iterate over "reader" variable and use this data to create a 2D list.
for row in reader:
    rowlist = []		
    for value in row:
        rowlist.append(value)
    environment.append(rowlist)
f.close()

# print(environment) # Used to test that "environment" contains "reader" data. 

# Create graph to plot agents and environnment on.
fig = matplotlib.pyplot.figure(figsize=(7, 7))  # Set the extent of the graph and assign it to variable "fig".
ax = fig.add_axes([0, 0, 1, 1])                 # Add axes to graph and assign them to variable "ax".

# Plot the initial state of "environment" on the above graph.
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()

# Make the agents.
for i in range(num_of_agents):
        agents.append(agentframework.Agent(environment, agents))

# Create "update" function to advance model one step.
def update(frame_number):
    fig.clear()
    
    # Create a for-loop to iterate over each agent, making them move, eat, share information and plot them on a graph. 
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
        
        # Plot the agents on the graph.
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
        
    # Shuffle the list of agents to prevent model artifacts (over-accumulation of wealth by the first agent).
    random.shuffle(agents)
        
# Animate the model using the FuncAnimation function from the matplotlib library, refreshing every 100 ms without repeating.
animation = matplotlib.animation.FuncAnimation(fig, update, interval=100, repeat=False, frames=num_of_iterations)
matplotlib.pyplot.show()   

# Used to test that "environment" had changed.
# matplotlib.pyplot.imshow(environment)  
# matplotlib.pyplot.show() 

# Save final environment state to "eatenEnvironment" file.
f2 = open('eatenEnvironment.csv', 'w', newline='') 
writer = csv.writer(f2, delimiter=' ')
for row in environment:		
	writer.writerow(row)
f2.close()

# Testing that the "move" function moves the agents.
'''
test_agent = agentframework.Agent(environment, agents)
#print(test_agent.y, test_agent.x)
test_agent.move()
#print(test_agent.y, test_agent.x)
'''
