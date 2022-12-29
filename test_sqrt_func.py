from sqrt_func import sqrt_func
import unittest

class TestSqrtFunc(unittest.TestCase):
	
	def test_valueerror(self):
		self.assertRaises(ValueError, sqrt_func, -1)
		self.assertRaises(ValueError, sqrt_func, -0.25)
		self.assertRaises(ValueError, sqrt_func, -9)
		
	def test_sqrt_func(self):
		self.assertEqual(sqrt_func(49), 7)
		self.assertEqual(sqrt_func(1.44), 1.2)
		self.assertEqual(sqrt_func(1), 1)
		self.assertEqual(sqrt_func(0.25), 0.5)
		self.assertEqual(sqrt_func(0), 0)
		
	def test_typeerror(self):
		self.assertRaises(TypeError, sqrt_func, [4, 9])
		self.assertRaises(TypeError, sqrt_func, 'A')
		
if __name__ == '__main__':
	unittest.main()
