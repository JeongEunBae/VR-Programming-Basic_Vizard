import viz
viz.go()

ground = viz.add('art/sphere_ground3.ive')
avatar = viz.add('vcc_female.cfg')

env = viz.add(viz.ENVIRONMENT_MAP,'sky.jpg')
dome = viz.add('skydome.dlc')
dome.texture(env)

viz.MainView.setPosition(0,1.8,5)
viz.MainView.setEuler(180,0,0)

avatar.state(4) #clapping mode

vizact.onkeydown( 'c', avatar.blend, 3,4,5 )
vizact.onkeydown( 's', avatar.blend, 3,0,5 )