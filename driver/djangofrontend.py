from driver.httpfrontend import HTTPFrontEnd


# This class handles all fetching from the Django upstream server
class DjangoFrontEnd(HTTPFrontEnd):

	def __init__(self, endpoint):
		HTTPFrontEnd.__init__(self, endpoint)

