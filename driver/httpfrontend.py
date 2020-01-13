import requests
import logging
from urllib.parse import urlencode
from urllib.request import Request, urlopen


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

	def post(self, name, params=None):
		if type(name) is not str:
			raise TypeError('program name needs to be a string')
		request = Request(self.__endpoint + name, urlencode(params).encode())
		logging.debug(request.full_url + " data: " + str(request.data))
		urlopen(request).read().decode()

	def get_endpoint(self):
		return self.__endpoint