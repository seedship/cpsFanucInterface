import json
from driver.httpfrontend import HTTPFrontEnd


# This class handles all fetching from the Django upstream server
class DjangoFrontEnd(HTTPFrontEnd):

	def __init__(self, endpoint):
		HTTPFrontEnd.__init__(self, endpoint + "/")

	def make_request(self):
		initparams = {"format": "json"}
		response = super().invoke_program("robot_position/", initparams)
		command = json.loads(response.content)
		return command

	def send_response(self, position_id, success):
		initparams = {"successful": str(success).lower(), "position": position_id}
		super().post("robot_response/", initparams)


