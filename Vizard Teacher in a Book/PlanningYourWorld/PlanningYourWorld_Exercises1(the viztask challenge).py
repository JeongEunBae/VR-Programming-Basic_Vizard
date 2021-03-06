##Bae Jeong Eun - Planning your world Exercises 1
import viz
import viztask

viz.go()

#Position the viewpoint.
viz.MainView.setPosition(0,1.8,6)
viz.MainView.setEuler(180,0,0)

woman = viz.addAvatar('vcc_female.cfg')
woman.state(1)

#Add a text message.
text = viz.addText('hit the spacebar to begin')
text.alignment( viz.TEXT_CENTER_BASE )
text.setEuler(180,0,0)
text.setScale(.3,.3,.3)
text.setPosition(0,2,0)
appear = vizact.fade(0,1,1)
disappear = vizact.fade(1,0,1)

#Add a balloon and an action for that balloon.
duck = viz.add('duck.cfg')
duck.setScale( .01,.01,.01) #modify-jeongeun
duck.setPosition(0,0,-5)
duck.state(1)
grow = vizact.size( 3,3,3,5, viz.TIME)
jump = vizact.animation(2)

#Add a woman who can walk away.
run = vizact.walkTo([10,0,10],verb='run') #modify-jeongeun

#1. Wait for the spacebar.
def wait_program():
	yield viztask.waitKeyDown(' ')

def instructions():
#2. Make the text fade away.
#This is the function you'll need to make the text visible.
#text.addAction( disappear )
	yield text.addAction(disappear)
	#Wait a second
	yield viztask.waitTime(1)
	
#3. Change the text to 'something is happening'.
	text.message('something is happening')
	
#4. Show the text and then hide the text.
#These are the functions you'll need to make the text visible.
#text.addAction( appear )
#text.addAction( disappear )
	#Add a fading action to the text and wait.
	yield viztask.addAction(text, vizact.fadeTo(1, time = 1))
	#Wait a second
	yield viztask.waitTime(1)
	#Wait to fade out.
	yield viztask.addAction(text, vizact.fadeTo(0, time = 1))
	
#5. Make the duck grow.
#This is the function you'll need to make the duck grow.
#duck.addAction( grow )
def duck_action():
	duck.addAction(grow)
	

#6. Make the duck jump.
#This is the function you'll need to make the duck hop.
#duck.execute( 2 )
	duck.addAction(jump)
	yield viztask.waitTime(6)
	
	
def run_woman():
#7. Make the woman run.
#This is the function you'll need to make the woman run away.
#woman.addAction( run )
	woman.addAction(run)
	

		
def main_sequence():
	while True:
		#Wait Key
		yield wait_program()
		
		yield instructions()
		
		yield duck_action()
		
		yield run_woman()
		
		
		
#Schedule the main sequence
viztask.schedule(main_sequence())