import requests

class FANUCFrontEnd:
	__endpoint = None

def __init__(self, endpoint):
	if type(endpoint) is not str:
		raise TypeError('endpoint needs to be a string')
	self.__endpoint = endpoint + "/KAREL/"

def begin_motion(self):
	initparams = {"task":"motion"}
	r = requests.get(url=self.__endpoint + "appstart", params=initparams)
	print(r.url)

def send_request(self, pos1, pos2, pos3, pos4, pos5, pos6, type):
	initparams = {
		"motion_t":type,
		"coord1": pos1,
		"coord2": pos2,
		"coord3": pos3,
		"coord4": pos4,
		"coord5": pos5,
		"coord6": pos6
	}
	r = requests.get(url=self.__endpoint + "appmove", params=initparams)
	print(r.url)
	pass