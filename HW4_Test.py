
import unittest

from HW4 import getRequest

class TestAPI(unittest.TestCase):

	def API_test(self):
		self.assertEqual(getRequest('Esethral', 5),"")
		self.assertEqual(getRequest('Esethral', 4),"Repo: TriangleTesting || Commits: 5\n")
		self.assertEqual(getRequest('Esethral', 3),"Repo: SSW-567-WS-Testing || Commits: 4\nRepo: TriangleTesting || Commits: 5\n")

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
