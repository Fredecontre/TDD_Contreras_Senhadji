import math
def sqrt_func(a):

	if (type(a) != float) and (type(a) != int) :
		raise TypeError('Input must be either int or float')
	
	if a < 0:
		raise ValueError('Input must be positive')
		
	return math.sqrt(a)
