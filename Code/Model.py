# -*- coding: utf-8 -*-
"""
Created on Sun May  2 10:51:29 2021

@author: Eliza
"""

# Import required libraries.
import tkinter
import matplotlib
matplotlib.use('TkAgg')
import requests
import bs4

import csv
import random
import matplotlib.pyplot
import agentframework
num_of_agents = 10      # Create variable and assign it a number of agents.
num_of_iterations = 100  # Create variable and assign it a number of iterations of the model.
neighbourhood = 20      # Create variable and assign it a value determining 'nearby' agents.
  
'''
root = tkinter.Tk()
root.wm_title("Model")

fig = matplotlib.pyplot.figure(figsize=(7, 7))  # Set the extent of the graph and assign it to variable "fig".
ax = fig.add_axes([0, 0, 1, 1]) 


canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
'''
'''
import tkinter

root = tkinter.Tk()   		# Main window.

c = tkinter.Canvas(root, width=200, height=200)
c.pack()			# Layout
c.create_rectangle(0, 0, 200, 200, fill="blue")


tkinter.mainloop()		# Wait for interactions.
'''

import tkinter
def run():
	pass

root = tkinter.Tk() 
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run) 

tkinter.mainloop()




''' 
# Create agent and environment variables.
agents = []
environment = []


# Open 'in.txt' file and save as variable "f".
f = open('in.txt', newline='')
# Parse "f" and save to "reader" variable.
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
'''

'''
# Iterate over "reader" variable and use this data to create a 2D list.
for row in reader:
    rowlist = []		
    for value in row:
        rowlist.append(value)
    environmen't.append(rowlist)
f.close()
'''
#import matplotlib.animation 

# Create parameters for ABM.''
# print(environment) # Used to test that "environment" contains "reader" data. 

# Create graph to plot agents and environnment on.
                # Add axes to graph and assign them to variable "ax".

# Plot the initial state of "environment" on the above graph.
#matplotlib.pyplot.imshow(environment)
#matplotlib.pyplot.show()
#canvas.show()

'''
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
'''  
# Animate the model using the FuncAnimation function from the matplotlib library, refreshing every 100 ms without repeating.
#animation = matplotlib.animation.FuncAnimation(fig, update, interval=100, repeat=False, frames=num_of_iterations)
#matplotlib.pyplot.show()   



def run():
    #animation = matplotlib.animation.FuncAnimation(fig, update, interval=100, repeat=False, frames=num_of_iterations)
  
    #canvas.show()
    
    menu_bar = tkinter.Menu(root)
    root.config(menu=menu_bar)
    model_menu = tkinter.Menu(menu_bar)
    menu_bar.add_cascade(label="Model", menu=model_menu)
    model_menu.add_command(label="Run model", command=run) 

    tkinter.mainloop()
    
    r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
    content = r.text
    soup = bs4.BeautifulSoup(content, 'html.parser')
    td_ys = soup.find_all(attrs={"class" : "y"})
    td_xs = soup.find_all(attrs={"class" : "x"})
    print(td_ys)
    print(td_xs)



# Used to test that "environment" had changed.
# matplotlib.pyplot.imshow(environment)  
# matplotlib.pyplot.show() 
'''
# Save final environment state to "eatenEnvironment" file.
f2 = open('eatenEnvironment.csv', 'w', newline='') 
writer = csv.writer(f2, delimiter=' ')
for row in environment:		
	writer.writerow(row)
f2.close()
'''
# Testing that the "move" function moves the agents.
'''
test_agent = agentframework.Agent(environment, agents)
#print(test_agent.y, test_agent.x)
test_agent.move()
#print(test_agent.y, test_agent.x)
'''
