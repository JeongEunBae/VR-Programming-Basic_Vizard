import viz
viz.go()

#First add a few models to the world.
ground = viz.add('art/sphere_ground3.ive')
rod = viz.add('art/rod.ive')
fish = viz.add('art/pike.ive')
barrel = viz.add('art/barrel.ive')
avatar = viz.add('vcc_male.cfg')

#Give the background a blue hue.
viz.clearcolor([.5, .6, 1])
#Place the viewpoint so we can see everything.
viz.MainView.setPosition(-7,1.5,.33)
viz.MainView.setEuler(90,0,0)

#make the fish a child node of the rod
fish.setParent(rod)
#Position and orient the fish on the rod.
fish.setPosition([.06, .04, 2.28], viz.ABS_PARENT)
fish.setEuler([0,-45,180], viz.ABS_PARENT)

fish.setScale([1,1,1.2], viz.ABS_LOCAL)

#Now move the rod up so that it's leaning against the barrel.
rod.setEuler([0.0,-50.0,0.0], viz.ABS_GLOBAL)
rod.setPosition([-0.04,0.13,-1.14],viz.ABS_GLOBAL)

#Move the fisherman.
avatar.setPosition(2,0,0)

#Add bees as a child node of the fisherman.
bees = fish.add('art/bees.ive') # exercises3. modify
#Place the bees at head level for the avatar.
bees.setPosition([0,0,0], viz.ABS_PARENT) # exercises3. modify

#now add afunction that will make the bees spin.
def swarm():
	bees.setEuler([5,0,0], viz.REL_PARENT)
vizact.ontimer(.01, swarm)

#And add a function that will
#make the avatar run.
import math
import time
avatar.state(11)

def run_around():
	newX = -math.cos(time.process_time()) * 2.1
	newZ = math.sin(time.process_time()) * 2.2
	avatar.setPosition([newX, 0, newZ], viz.ABS_PARENT)
	avatar.setEuler([time.process_time()/math.pi*180,0,0], viz.ABS_PARENT)
vizact.ontimer(.01, run_around)

#Link the view to the avatar's head (exercises 4.)
head_bone = avatar.getBone('Bip01 Head')
view_link = viz.link(head_bone, viz.MainView)
viz.MainView.eyeheight(0)