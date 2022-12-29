import math 

def triangle_compute(a, b, c):

	if type(a) != int and type(a) != float and type (b) != int and type(b) != float and type(c) != int and type(c) != float :
		raise TypeError('Side lengths must be either int or float')
	
	if a + b < c: 
		raise ValueError('Incorrect side lengths')
	elif b + c < a:
		raise ValueError('Incorrect side lengths')
	elif c + a < b:
		raise ValueError('Incorrect side lengths')
		
	if a <= 0 or b <= 0 or c <= 0:
		raise ValueError('Side length must be positive')

	alpha = round((math.acos((b*b + c*c - a*a)/ (2*b*c)) * 180/math.pi), 2)
	beta = round((math.acos((a*a + c*c - b*b)/ (2*a*c)) * 180/math.pi), 2)
	gamma = round((math.acos((a*a + b*b - c*c)/ (2*a*b)) *180/math.pi), 2) 
	
	return [alpha, beta, gamma]
