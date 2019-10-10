
import unittest

from HW4 import getRequest

class TestAPI(unittest.TestCase):

	def API_test(self):
		self.assertEqual(getRequest('esethral', 5),"", "Invalid")
		self.assertEqual(getRequest('esethral', 4),"Repo: TriangleTesting || Commits: 5\n", "Invalid")
		self.assertEqual(getRequest('esethral', 3),"Repo: SSW-567-WS-Testing || Commits: 4\nRepo: TriangleTesting || Commits: 5\n", "Invalid")

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
