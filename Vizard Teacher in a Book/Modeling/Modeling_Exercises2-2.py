import viz
viz.go()

#Place the viewpoint 
viz.MainView.setPosition(1.5,1.8,-5)
barrels = [] #barrels 

#bottom barrels 
for index in range(3):
	barrel = viz.add('art/barrel.ive')
	barrel.setPosition([index * 1,0,0])
	
	barrels.append(barrel)
	
#middle barrels	
for index in range(2):
	barrel = viz.add('art/barrel.ive')
	barrel.setParent(barrels[0])
	barrel.setPosition([index * 1 + .5,1.0,0], viz.ABS_PARENT)

	barrels.append(barrel)

#top barrels
barrel = viz.add('art/barrel.ive')
barrel.setParent(barrels[3])
barrel.setPosition([.5,1.0,0], viz.ABS_PARENT)

barrels.append(barrel)
