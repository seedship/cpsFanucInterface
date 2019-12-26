import requests
import logging


class HTTPFrontEnd:
	__endpoint = None

	def __init__(self, endpoint):
		if type(endpoint) is not str:
			raise TypeError('endpoint needs to be a string')
		self.__endpoint = endpoint

	def invoke_program(self, name, params=None):
		if type(name) is not str:
			raise TypeError('program name needs to be a string')
		r = requests.get(url=self.__endpoint + name, params=params)
		logging.debug(r.url)
		return r
