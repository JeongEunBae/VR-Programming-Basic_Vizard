import viz
viz.go()

#Set the position of the view.
viz.MainView.setPosition(0, 2, 0)
viz.MainView.setEuler(0, 90, 0)

#Set the background color.
viz.clearcolor([.3,.3,.3])

#Add the spider avatar
first_spider = viz.add('art/spider/spider1.cfg')
first_spider_bone = first_spider.getBone('bone_root')
first_spider.texture(viz.addTexture('art/spider/euro_cross.tif'))
first_spider.setScale(.02,.02,.02)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
#Animate the spider's lefs.
first_spider.state(2)

#Animate the spider travelling
#in a spiral path.
first_increment = 0
C = 0.01
import math
def move_first_spider():
	global first_increment
	#Increase the increment every
	#time the function is executed.
	first_increment += .005
	#Use some trig to place the
	#spider on the spiral.
	x = C*first_increment*math.cos(first_increment)
	z = C*first_increment*math.sin(first_increment)
	first_spider.setPosition([x,0,z])
	#Find the increment the spider
	#shoud be facing.
	face_angle = vizmat.AngleToPoint([0,0], [x,z]) -90
	first_spider.setEuler([face_angle, 0, 0])
	
#Call the move_spider function every
#hundredth of a second.
vizact.ontimer(.005, move_first_spider)

#Start an on-the-fly object for the web.
viz.startLayer(viz.LINE_STRIP)
viz.vertex(0,0,0)
myweb = viz.endLayer()

#Make the object dynamic, since we'll
#be adding to it.
myweb.dynamic()

#Add the next vertex and link it to
#the spider.
current_vertex = myweb.addVertex([0,0,0])
web_link = viz.link(first_spider, myweb.Vertex(0))

def lay_web():
	#This function will lay the most
	#recent vertex of the web down.
	#WE make these variables global
	#because we'll be changing them.
	global web_link, current_vertex
	
	#Remove the current link between
	#web and spider.
	web_link.remove()
	
	#Set the vertex at the spider's
	#current location.
	myweb.setVertex(current_vertex, first_spider.getPosition())
	
	#Add a new vertex and link it
	#to the spider.
	current_vertex = myweb.addVertex(first_spider.getPosition())
	web_link = viz.link(first_spider_bone, myweb.Vertex(current_vertex))
	
#Call the function on a timer
vizact.ontimer(.5, lay_web)