#Define the class.
class make_car:
	def __init__(self):
		#Initialize the class .
		#This method will be called
		#when you first instantiate
		#an object
		self.moving = False
	
	def peel_out(self):
		#This function can
		#be called from within
		#or utside of the
		#class. It will print
		#something and change the
		#object's moving variable.
		
		print('vroom')
		print('vroooom')
		print('VROOOOOOOOOOOM')
		self.moving = True

class driver(make_car):
	def leave_town(self):
		print('I am out of here')
		#Call an inherited method.
		self.peel_out()
		
#Instantiate an object using
#the make_car class.
#my_car = make_car()

#Call a function in the object.
#my_car.peel_out()
#print(my_car.moving)

#Instantiate an object using
#driver class.
my_driver = driver()

#Call a method in the object.
my_driver.leave_town()
#Refer to one of my_driver's
#inherited variables.
print(my_driver.moving)