from list_min import list_min
import unittest

class TestListMin(unittest.TestCase):

	def test_valueerror(self):
		self.assertRaises(ValueError, list_min, [])
		
	def test_list_min(self):
		self.assertEqual(list_min([12]), 12)
		self.assertEqual(list_min([23, 15, 3, 7, 11]), 3)
		self.assertEqual(list_min([8, 6, 4, 2, 0]), 0)
		self.assertEqual(list_min([-55, -40, -30, 0]), -55)
		self.assertEqual(list_min([10, 9, -4, 22, 0]), -4)
		
	def test_typeeerror(self):
		self.assertRaises(TypeError, list_min, [0.5, 1, 0])
		self.assertRaises(TypeError, list_min, ['a', 23, -4])
		
if __name__ = '__main__':
	unittest.main()
		
		
