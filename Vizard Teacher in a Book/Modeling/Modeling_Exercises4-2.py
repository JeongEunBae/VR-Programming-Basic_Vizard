import viz
viz.go()

lights = []
	
def bowling_ball():
	# Add a model
	ball = viz.add('art/white_ball.wrl')

	ball.setPosition(0, 1.8, 2)
	
	#Add a light 
	bowling_light = viz.addLight()
	bowling_light.position(0,0,-1,1)
	bowling_light.color(viz.GREEN)
	bowling_light.intensity(10)
	ball.shininess(20)
	
	viz.link(ball, bowling_light)
	
	lights.append(bowling_light)
	
def sun():
	# Add a model
	ball = viz.add('art/white_ball.wrl')

	ball.setPosition(0, 1.8, 2)
	
	#Add a light 
	sun_light = viz.addLight()
	sun_light.position(0,0,-1,0)
	sun_light.color(viz.RED)
	sun_light.intensity(100)
	ball.specular(viz.ORANGE)
	ball.ambient(viz.ORANGE)
	
	viz.link(ball, sun_light)
	
	lights.append(sun_light)
	
def cherry():
	# Add a model
	ball = viz.add('art/white_ball.wrl')

	ball.setPosition(0, 1.8, 2)
	
	#Add a light 
	cherry_light = viz.addLight()
	cherry_light.position(0,0,-1,1)
	cherry_light.color(viz.RED)
	ball.emissive(viz.RED)
	cherry_light.intensity(100)
	ball.shininess(1)
	
	viz.link(ball, cherry_light)
	
	lights.append(cherry_light)
	
def reset():
	for light in lights:
		light.disable()
		
vizact.onkeydown('1', bowling_ball)
vizact.onkeydown('2', sun)
vizact.onkeydown('3', cherry)
vizact.onkeydown('r', reset)