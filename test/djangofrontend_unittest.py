import unittest

from driver.djangofrontend import DjangoFrontEnd


class DjangoFrontEndUnitTest(unittest.TestCase):
	djangofrontend = DjangoFrontEnd("http://127.0.0.1:8000")

	def test_dummy(self):
		res = self.djangofrontend.make_request()
		print(res)


if __name__ == '__main__':
	unittest.main()
