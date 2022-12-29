def list_min(int_list):
	n = len(int_list)
	
	if n <= 0:
		raise ValueError('Empty List')

	min = int_list[0]
	for i in range(n):
	
		if type(int_list[i]) != int:
			raise TypeError('List element is not an integer')
			
		if int_list[i] < min:
			min = int_list[i]
	
	return min
