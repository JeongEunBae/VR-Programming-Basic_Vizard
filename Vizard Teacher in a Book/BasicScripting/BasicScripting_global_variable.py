#Define a global variable.
season = 'spring'

#Define a funtion
def worker_bee():
	if season == 'spring':
		return 'honey'
		
	else:
		return 'I got nothing'
		
		
#Call the function and store
#the returned value as "bee_response".
bee_response = worker_bee()
print(bee_response)

#----------------------------------

def fruitless():
	global apple # global variable 
	apple = 'hello' #local variable
	
fruitless()
print(apple)

#----------------------------------

value = "hello" # local variable

def change_variable():
	value = 'goodbye'
	print('local', value)
	
change_variable()
print('global', value)

#----------------------------------

value_1 = "hello" 

def change_variable():
	global value_1 # global variable 
	value_1 = 'goodbye'
	print('local', value_1)
	
change_variable()
print('global', value_1)