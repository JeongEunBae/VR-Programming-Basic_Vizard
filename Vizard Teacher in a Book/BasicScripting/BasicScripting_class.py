#Define a class
class most_basic:
	whatever = 'original value'

#Use the class to instantiate
#two objects.

one_object = most_basic()
another_object = most_basic()

#Change the variable
#in one of the objects.
one_object.whatever = 'changed value'

#Now print out the variable
#from each object. Notice that
#they have different values
# (we changed "whatever" in one but not the other).

print(one_object.whatever)
print(another_object.whatever)