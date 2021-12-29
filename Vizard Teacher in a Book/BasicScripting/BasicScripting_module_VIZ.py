import viz

#Use the viz module's go
#function to render a 3D
#world in a graphics
#window.
viz.go()

#Use a for loop to ...
for i in range(5):
	#use the viz module
	#to add a 3D model.
	#The viz.add method
	#will return a node3d object.
	ball = viz.add('white_ball.wrl')
	
	#Use a node3D method
	#to place the object
	#in the world.
	
	ball.setPosition(i * .2, 1.8, 3)
	