from driver.httpfrontend import HTTPFrontEnd
import json


# This class handles all invocations to the FANUC robot
class FANUCFrontEnd(HTTPFrontEnd):

	def __init__(self, endpoint):
		super().__init__(endpoint + "/KAREL/")

	def start_motion(self):
		response = super().invoke_program("appmotion")
		return self.__validateSuccess(response)

	def stop_motion(self):
		response = super().invoke_program("appabort")
		return self.__validateSuccess(response)

	def send_motion_request(self, pos1, pos2, pos3, pos4, pos5, pos6, type):
		initparams = {
			"motion_t": type,
			"coord1": pos1,
			"coord2": pos2,
			"coord3": pos3,
			"coord4": pos4,
			"coord5": pos5,
			"coord6": pos6
		}
		response = super().invoke_program("appmove", initparams)
		return self.__validateSuccess(response)

	def reset(self):
		response = super().invoke_program("appreset")
		return self.__validateSuccess(response)

	def get_status(self):
		response = super().invoke_program("appmonitor")
		return json.loads(response.text)

	def rotate(self):
		initparams = {"task": "rotate"}
		super().invoke_program("appstart", initparams)

	def __validateSuccess(self, response):
		try:
			response_json = json.loads(response.text)
			return response_json["result"] == "success"
		except:
			return False