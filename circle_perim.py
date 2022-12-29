import math
def circle_perim(radius):

	if (type(radius) != float) and (type(radius) != int) :
		raise TypeError('Input must be either int or float')
	
	if radius <= 0:
		raise ValueError('Input must be positive')
		
	return 2*math.pi*radius
