import viz
viz.go()

#Add a model of a forest.
forest = viz.add('art/forest.ive')

#Add an avatar to stand there idly.
a = viz.addAvatar('vcc_male.cfg')
a.setEuler([20,0,0])
a.setPosition([-.78,0,.3])
a.state(1)

#Set the viewpoint's position and
#orientation so that we'll be able to see our scene.
viz.MainView.setPosition([-.75,1.8,4.2])
viz.MainView.setEuler([-180,4,0])

#Disable the default head light.
viz.MainView.getHeadLight().disable()

#Add a model of a torch and place it in the scene.
spotlight = viz.add('art/flashlight.IVE')
spotlight.setPosition( [-.78,3,-0.5])
spotlight.setEuler([0,90,0]) # flash_light rotate

#Add a light for the torch.
flash_light = viz.addLight()
#Make the light positional.
flash_light.position(0,1,0,1) 
#Make this positional light a spot light by
#limiting its spread.
flash_light.intensity(100) # intensity
flash_light.spread(20)
flash_light.spotexponent(20)

#Link the light source to the torch.
viz.link(spotlight, flash_light)