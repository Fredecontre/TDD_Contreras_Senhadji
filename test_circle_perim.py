from circle_perim import circle_perim 
import unittest
import math

class TestCirclePerim(unittest.TestCase):
	
	def test_valueerror(self):
		self.assertRaises(ValueError, circle_perim, 0)
		self.assertRaises(ValueError, circle_perim, -0.5)
		self.assertRaises(ValueError, circle_perim, -10)
		
	def test_circle_perim(self):
		self.assertEqual(circle_perim(0.4), 2*math.pi*0.4)
		self.assertEqual(circle_perim(1), 2*math.pi)
		self.assertEqual(circle_perim(5.33), 2*math.pi*5.33)
		
	def test_typeerror(self):
		self.assertRaises(TypeError, circle_perim, [])
		self.assertRaises(TypeError, circle_perim, 'Hello')
		self.assertRaises(TypeError, circle_perim, -2.4+0.8j)
		
if __name__ == '__main__':
	unittest.main()
