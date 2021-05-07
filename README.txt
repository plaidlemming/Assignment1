Contents:

- 'Code' folder contains: 
	- Model.py (main source code)
	- agentframework.py (agent source code)
	- int.tx (environment data)

This software is an agent-based model in which the agents move around the envionment and deplete it, while communicating with each other.

How to run:
	- Open the the code folder in your chosen Python IDE
	- Run program.

When the software runs it will:
	- Take in the int.tx data to form the environment
	- Generate an animation of agents' movement in a new window (could represent sheep in a field)
	- Create a new file called 'eatenEnvironments' to show the final environment state after manipulation by the agents.

For further development, a property attribute could be implemented to protect the 'self' variables using 'fget' and 'fset' functions (code outlined in agentframework.py).

An attempt was made to create a GUI to allow users to input their own model parameters without editing the souce code. This was unsuccessful, but the code is in the other branch (assignment-1-updates).