import viz
viz.go()

#Add the ground and an avatar.
ground = viz.add('art/sphere_ground.ive')
avatar = viz.addAvatar( 'vcc_female.cfg' )
#Make the avatar idle.
avatar.state(1)

#Add some balloons.
balloons = []
#Import the python random module to make 
#some features of the balloon random.
import random
for i in range(-5,6):
	for j in range(1,6):
		#Add and adjust the appearance and 
		#position of several balloons.
		balloon = viz.add('art/balloon.ive')
		balloon.setPosition( i*.8,.1,j*.8 )
		R = random.random()
		G = random.random()
		B = random.random()
		balloon.color( R, G, B )
		balloon.specular( viz.WHITE )
		balloon.shininess( 128 )
		balloons.append( balloon )

#Add a sky with an environment map.
env = viz.add(viz.ENVIRONMENT_MAP,'sky.jpg')
dome = viz.add('skydome.dlc')
dome.texture(env)

#Add some audio files.
inflate_sound = viz.addAudio( 'art/blowballoon.wav')
deflate_sound = viz.addAudio( 'art/deflateballoon.wav')

#Add lighting and remove the head light.
for p in [1,-1]:
	light = viz.addLight()
	light.position( p,1,p,0 ) 
viz.MainView.getHeadLight().disable()

#Position the viewpoint.
viz.MainView.setPosition([0,1.2,-8.9])
viz.MainView.setEuler([0,-12,0])


#Set constants for actions.
INFLATED = [2,2,2]
DEFLATED = [.2,.2,.2]
BREATH_LENGTH = 3
DEFLATE_LENGTH = .1

#Create actions to animation the inflation of a balloon (any balloon).
grow = vizact.size( INFLATED, BREATH_LENGTH, viz.TIME )
play_blowing_sound = vizact.call( inflate_sound.play )
inc_transparent = vizact.fade( 1, .7, BREATH_LENGTH )
#Pull together parallel actions into single actions.
inflate = vizact.parallel( grow, play_blowing_sound, inc_transparent ) 

#Create actions for floating away.
float_away = vizact.move( vizact.randfloat(-.2,.2), 1, vizact.randfloat(-.2,.2),8 )
float_away_forever = vizact.move( vizact.randfloat(-.2,.2), 1, vizact.randfloat(-.2,.2) )


#Create actions to animate a balloon deflating.
shrink = vizact.size( DEFLATED, DEFLATE_LENGTH, viz.TIME ) 
play_def = vizact.call( deflate_sound.play ) 
dec_transparent = vizact.fade( .7,1, DEFLATE_LENGTH )
#Pull together parallel actions into a single action for deflation.
deflate = vizact.parallel( shrink, play_def, dec_transparent )

#Create a falling action.
fall = vizact.fall( 0 )

#Create an action that will wait a random amount of time.
random_wait = vizact.waittime( vizact.randfloat(.5,7) )

#Create the lifecycle of the balloon with a sequence.
life_cycle = vizact.sequence( [random_wait, inflate, float_away, deflate, fall], 1 )

#Add the actions to our balloons.
for balloon in balloons:
	balloon.setScale( DEFLATED )
	vizact.onkeydown( ' ', balloon.addAction, life_cycle ) 

