import viz
viz.go()

viz.MainView.setPosition(0, .68, -1.3)
#Add a model
wall = viz.add('art/wall.ive')

#Add the texture files
stone_wall = viz.addTexture('art/stone wall.jpg')
pine_needles = viz.addTexture('art/pine needles.jpg')

#Apply texture to model 
wall.texture(stone_wall, '', 0)
wall.texture(pine_needles, '', 1)

#wrap mode - repeat
stone_wall.wrap(viz.WRAP_S, viz.REPEAT)
stone_wall.wrap(viz.WRAP_T, viz.REPEAT)

matrix = vizmat.Transform()
def change_texture_matrix(value_S, value_T):
	current_scale = matrix.getScale()
	current_scale[0] = value_S
	current_scale[1] = value_T
	matrix.setScale(current_scale)
	
	wall.texmat(matrix, '', 0)
	
change_texture_matrix(5, 5)

#Add a slider and put it on
#the bottom of the screen.
slider = viz.addSlider()
slider.setPosition(.5, .1)

def swap_textures(slider_position):
	pine_needles_amt = slider_position
	#Blend the clouds (unit #1) in that amount.
	wall.texblend (pine_needles_amt, '', 1)
	
#Set up the alider event to call our function.
vizact.onslider(slider, swap_textures)
#Set the initial blend to match the slider.
swap_textures(0)


