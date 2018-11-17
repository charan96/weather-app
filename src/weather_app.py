import json
import urllib2
import tabulate
from collections import OrderedDict

from url_constructor import URLConstructor


class WeatherApp:
	def __init__(self):
		self.urlc = URLConstructor()

	def generate_url(self, zipcode):
		return self.urlc.generate_url(zipcode)

	def get_url_response(self, zipcode):
		json_response = urllib2.urlopen(self.urlc.generate_url(zipcode)).read()
		
		if json.response['cod'] == 200:
			return json_response
		elif json.response['cod'] == 429:
			raise RuntimeError('exceded API request limit; {}'.format(json_response))
		else:
			raise RuntimeError('{}'.format(json_response))
	
	def get_relevant_info(self, json_response):
		info = OrderedDict()

		info['condition'] = json_response['weather']['main']
		info['temperature'] = (9/5) * (json_response['main']['temp'] - 273) + 32
		info['wind'] = json_response['wind']['speed']
		info['humidity'] = json_response['main']['humidity']
		info['cloudiness'] = json_response['clouds']['all']

		return info.items()
		
	def get_weather(self, zipcode):
		json_response = self.get_url_response(zipcode)
		return tabulate.tabulate(self.get_relevant_info(json_response))		
				
