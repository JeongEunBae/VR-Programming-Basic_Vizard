import vizact
import viz

#Import the vizjoy module and add one joystick.
import vizjoy
joy = vizjoy.add()

def update_joystick():
	#Get the joystick position
	x,y,z = joy.getPosition()
	#Get the twist of the joystick
	twist = joy.getTwist()
	#Move the viewpoint forward/
	#backward based on y-axis value
	#Make sure value is above a certain 
	#threshold.
	if abs(x) > 0.2: 
		viz.MainView.move(0,0,x*0.01,viz.BODY_ORI)
	#Move the viewpoint left/right based 
	#on x-axis value. Make sure value is 
	#above a certain threshold
	if abs(y) > 0.2: 
		viz.MainView.move(y*0.01,0,0,viz.BODY_ORI)
	#Turn the viewpoint left/right based 
	#on twist value. Make sure value is 
	#above a certain threshold.
	if abs(twist) > 0.2: 
		viz.MainView.rotate(0,1,0,twist,viz.BODY_ORI,viz.RELATIVE_WORLD)

#UpdateJoystick every frame
vizact.ontimer(0,update_joystick)