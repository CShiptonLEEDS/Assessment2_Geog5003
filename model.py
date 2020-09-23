# -*- coding: utf-8 -*-
"""
Show me the way to go home...
"""
import matplotlib
import matplotlib.pyplot
import agentframework
import csv

#Creating the environment that will represent the town
#Create a list of agents from the agentframework 

environment = []
drunk = []

no_of_drunks = 10 # controls how many agents we have
no_of_iterations = 100 # changes the agent coordinates a number of times

#Add the map of the town that shows the locations

f=open('drunkplan.txt', newline='') # read the text a line at a time
reader=csv.reader (f, quoting = csv.QUOTE_NONNUMERIC) # convert to float
for row in reader: #reading in the rows a row at a time
    rowlist = []
    for item in row:
        rowlist.append(item)
    environment.append(rowlist)
f.close()

print(type(environment), len(environment))

# Create the map environment (mapenvironment) in order to map density of each point of the map
# When an agent passes through a point on the map, needs to be calculated, and saved

mapenvironment = []
    
height=len(environment)
width=len(environment[0])

for i in range(height):
    rowlist = []
    for j in range(width):
        rowlist.append(0)
    mapenvironment.append(rowlist)

# Assign the drunks using the class that has been created
# Tell each drunk that their house number is their own agent number plus one, then multiplied by 10

for i in range(no_of_drunks):
    house = (i+1)+1
    drunk.append(agentframework.Drunk(environment, drunk, house))

# Move each drunk
# If they aren't home, then the drunk continue on until they reach their endpoint
# If they haven't reached their home, then add 1
    
for i in range(no_of_drunks):
    while drunk[i].home==False:
        drunk[i].move()
        mapenvironment[drunk[i].x][drunk[i].y]+=1
    if drunk[i].house==drunk[i].environment[drunk[i].x][drunk[i].y]:
        drunk[i].home==True
        
# Plot graph of initial positions of each agent
matplotlib.pyplot.ylim(0, len(environment[0]))
matplotlib.pyplot.xlim(0, len(environment))
matplotlib.pyplot.imshow(environment)
for drunk in range(no_of_drunks): 
        matplotlib.pyplot.scatter(drunk[drunk].x,drunk[drunk].y)  
        matplotlib.pyplot.show()        

# Save the density map to a file as text

f2 = open('map.csv', 'w', newline='')
writer = csv.writer(f2, delimiter=' ')
for row in mapenvironment:
    writer.writerow(row)
f2.close()