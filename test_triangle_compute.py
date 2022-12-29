from triangle_compute import triangle_compute
import unittest
import math

class TestTriangleCompute(unittest.TestCase):
	
	def test_valueerror(self):
		# side length condition
		self.assertRaises(ValueError, triangle_compute, 2, 3, 4)
		# null value
		self.assertRaises(ValueError, triangle_compute, 0, 1, 2)
		# negative value
		self.assertRaises(ValueError, triangle_compute, -1, 2, 3)
	
	def test_triangle_compute(self):
		# triangle lambda
		self.assertEqual(triangle_compute(3.2, 4.1, 6.3),[26.43 ,34.77 , 118.80])
		# triangle isocèle 
		self.assertEqual(triangle_compute(1,1,1),[60.00, 60.00, 60.00])
		# triangle equilateral
		self.assertEqual(triangle_compute(1,1,0.5),[75.52, 75.52, 28.96])
		# triangle rectangle
		self.assertEqual(triangle_compute(3,4,5),[36.87, 53.13, 90.00])
		# triangle rectangle et isocèle
		self.assertEqual(triangle_compute(2,2,math.sqrt(8)),[45.00, 45.00, 90.00])
	
	def test_typeerror(self):
		self.assertRaises(TypeError, triangle_compute, 3, 4, '5')
		self.assertRaises(TypeError, triangle_compute, [1, 1, 1], [], [])
		self.assertRaises(TypeError, triangle_compute, 3, 4,  )
	
if __name__ == '__main__':
	unittest.main()
