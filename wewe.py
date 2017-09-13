import unittest

def subtract_one(input_integer):
	return input_integer - 1

class FunctionTests(unittest.TestCase):
	def setup(self):
		pass

	def test_subtr_function(self):
		self.assertEqual(
			subtract_one(3),2, 
			"Testing if my")

	def Test_neg(self):
		self.assertEqual(
			subtract_one(0), 0, 
			"Testing funciton with 0")


unittest.main(verbosity=2)
