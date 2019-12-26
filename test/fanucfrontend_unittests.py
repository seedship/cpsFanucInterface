import logging
import unittest

from driver.fanucfrontend import FANUCFrontEnd
from io import StringIO


# Unit tests for FanucFrontEnd to ensure http requests are properly formed
class FanucFrontEndUnitTest(unittest.TestCase):
	log_stream = None
	frontend = FANUCFrontEnd("http://hookbin.com")

	def setUp(self):
		logger = logging.getLogger()
		logger.propagate = False
		logger.level = logging.DEBUG

		self.log_stream = StringIO()
		string_handler = logging.StreamHandler(self.log_stream)
		string_handler.addFilter(lambda r: r.name == "root")
		logger.addHandler(string_handler)

		# Uncomment to have http URLs printed to terminal. Import sys to use
		# stream_handler = logging.StreamHandler(sys.stdout)
		# stream_handler.addFilter(lambda r: r.name == "root")
		# logger.addHandler(stream_handler)

	def tearDown(self):
		self.log_stream = None

	def test_begin_motion(self):
		self.frontend.begin_motion()
		self.assertEqual(self.log_stream.getvalue(), "https://hookbin.com/KAREL/appstart?task=motion\n")

	def test_send_motion(self):
		self.frontend.send_motion_request(1,2,3,4,5,6,"jjr")
		self.assertEqual(self.log_stream.getvalue(), "https://hookbin.com/KAREL/appmove?motion_t=jjr&coord1=1&coord2=2&coord3=3&coord4=4&coord5=5&coord6=6\n")

	def test_abort(self):
		self.frontend.stop_motion()
		self.assertEqual(self.log_stream.getvalue(), "https://hookbin.com/KAREL/appabort\n")


if __name__ == '__main__':
	unittest.main()
