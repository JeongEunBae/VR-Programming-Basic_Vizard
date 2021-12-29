#loop_FOR_array

#Define an array.
#my_array = ['a', 'b', 'c'] 
my_array = range(5)

#Loop through every element in
#my_array
for element in my_array:
	print('current element is', element)
	if element == 4:
		print('all done')
	else:
		print('wait, there is more')
	