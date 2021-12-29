import viz
import random
viz.go()

#Add the models.
ground = viz.add('art/sphere_ground3.ive')
ball = viz.add('art/white_ball.wrl')
ball.setPosition(0,3,.5)

#Add a sky.
env = viz.add(viz.ENVIRONMENT_MAP, 'sky.jpg')
dome = viz.add('skydome.dlc')
dome.texture(env)

#Set the viewpoint
viz.MainView.setPosition(0,1.8,7)
viz.MainView.setEuler(180, 0, 0)

#Enable the physics enine.
viz.phys.enable()

#Define some physics components.
ball_collide_shape = ball.collideBox()
ground.collidePlane( 0,1,0,0 )

ball_collide_shape.bounce = 1.5

ball.enable(viz.COLLIDE_NOTIFY)
 
#Define a function of collision event 
def onColide(e): # Exercise2 
	R = random.random()
	G = random.random()
	B = random.random()
	ball.color(R, G, B)
		

viz.callback(viz.COLLIDE_BEGIN_EVENT, onColide)

#reset ball
def reset():
	ball.setPosition(0,3,.5)
	ball.color(viz.WHITE)

vizact.onkeydown('r', reset)