from driver.httpfrontend import HTTPFrontEnd


# This class handles all invocations to the FANUC robot
class FANUCFrontEnd(HTTPFrontEnd):

	def __init__(self, endpoint):
		super().__init__(endpoint + "/KAREL/")

	def begin_motion(self):
		initparams = {"task":"motion"}
		super().invoke_program("appstart", initparams)

	def stop_motion(self):
		super().invoke_program("appabort")

	def send_motion_request(self, pos1, pos2, pos3, pos4, pos5, pos6, type):
		initparams = {
			"motion_t":type,
			"coord1": pos1,
			"coord2": pos2,
			"coord3": pos3,
			"coord4": pos4,
			"coord5": pos5,
			"coord6": pos6
		}
		super().invoke_program("appmove", initparams)

	def rotate(self):
		initparams = {"task":"rotate"}
		super().invoke_program("appstart", initparams)
