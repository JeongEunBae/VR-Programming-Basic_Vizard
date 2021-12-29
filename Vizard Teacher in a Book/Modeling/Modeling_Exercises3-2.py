import viz
viz.go()

balloons = []

for i in range(4):
	balloon = viz.add('art/balloon.ive') 	#add a model
	balloon.setPosition( i, .1, .8) #set position
	
	balloons.append(balloon)				#append balloon in array balloons

balloons[0].color(viz.GREEN)				#set color
balloons[1].color(viz.RED)
balloons[2].color(viz.BLUE)
balloons[3].color(viz.YELLOW)


inflate_sound = viz.addAudio('art/blowballoon.wav')

for p in [1,-1]:
	light = viz.addLight()
	light.position(p,1,p,0)
viz.MainView.getHeadLight().disable()
	
viz.MainView.setPosition([1.2,-3,-11])
viz.MainView.setEuler([0,-12,0])

INFLATED = [3,3,3]
BREATH_LENGTH = 3

grow = vizact.size(INFLATED,BREATH_LENGTH,viz.TIME)
play_blowing_sound = vizact.call(inflate_sound.play)
inc_transparent = vizact.fade(1, .7, BREATH_LENGTH)#
inflate = vizact.parallel(grow, play_blowing_sound, inc_transparent)

life_cycle_balloon = vizact.sequence([inflate], 1)

vizact.onkeydown('g', balloons[0].addAction, life_cycle_balloon)
vizact.onkeydown('r', balloons[1].addAction, life_cycle_balloon)
vizact.onkeydown('b', balloons[2].addAction, life_cycle_balloon)
vizact.onkeydown('y', balloons[3].addAction, life_cycle_balloon)