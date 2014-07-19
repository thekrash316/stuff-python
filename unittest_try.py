import unittest


def factorial(n):
	if n < 0:
		raise ValueError("invalid input: " + str(n))

	if n == 0 or n == 1:
		return 1

	return n * factorial(n-1)


class FactorialTest(unittest.TestCase):

	def testFactorialOfZero(self):
		self.assertEqual(1, factorial(0))


	def testFactorialOfOne(self):
		self.assertEqual(1, factorial(1))


	def testFactorialOfAPositive(self):
		self.assertEqual(2, factorial(2))
		self.assertEqual(3*2, factorial(3))
		self.assertEqual(8*7*6*5*4*3*2, factorial(8))
		self.assertEqual(10*9*factorial(8), factorial(10))


	def testFactorialOfANegative(self):
		self.assertRaises(ValueError, factorial, -1)

		self.assertRaisesRegexp(ValueError, '^invalid input:.*$', factorial, -3)


if __name__ == '__main__':
	unittest.main()
