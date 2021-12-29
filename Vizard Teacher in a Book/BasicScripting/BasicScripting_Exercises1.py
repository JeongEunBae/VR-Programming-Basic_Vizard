#BASIC SCRIPTING EXERCISES-1
import viz
import random
viz.go()

balloons = []
colors = [viz.GREEN, viz.RED, viz.BLUE, viz.YELLOW, viz.ORANGE] # balloon color

def inflate(who): #balloons inflate
	inflate_animation = vizact.size(2,2,2)
	#Add the action to the node
	who.addAction(inflate_animation)
	who.color(viz.PURPLE) #change color(purple)
	
for i in range(-3, 3):
	#Add a model
	balloon = viz.add('art/balloon.ive')
	
	#Set Position
	balloon.setPosition( i, 1.8, 3)
	
	balloons.append(balloon)

#Change each balloon's color
for balloon in balloons:
	balloon.color(random.choice(colors)) # random color
	vizact.onkeydown('b', inflate, balloon) # balloon inflate -> change Purple color
