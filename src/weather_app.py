import json
import requests
import tabulate
from collections import OrderedDict

from .url_constructor import URLConstructor


class WeatherApp:
	def __init__(self, config):
		self.config = config
		self.urlc = URLConstructor(config.get_api_key())

	def generate_url(self, zipcode):
		return self.urlc.generate_url(zipcode)

	def get_url_response(self, zipcode):
		response = requests.get(self.urlc.generate_url(zipcode))
		
		if response.status_code == 404:
			raise ValueError('invalid zip code')

		json_response = response.json()
		
		if json_response['cod'] == 200:
			return json_response
		elif json_response['cod'] == 429:
			raise RuntimeError('exceded API request limit; {}'.format(json_response))
		else:
			raise RuntimeError('{}'.format(json_response))
	
	def get_relevant_info(self, json_response):
		info = OrderedDict()

		info['Location'] = json_response['name']
		info['Condition'] = json_response['weather'][0]['main']
		info['Temperature'] = format((9/5) * (json_response['main']['temp'] - 273) + 32, '.1f') + ' F'
		info['Wind'] = format(json_response['wind']['speed'] * 2.2369, '.1f') + ' mph'
		info['Humidity'] = str(json_response['main']['humidity']) + '%'
		info['Cloudiness'] = str(json_response['clouds']['all']) + '%'

		return info.items()
		
	def get_weather(self, zipcode):
		json_response = self.get_url_response(zipcode)
		return tabulate.tabulate(self.get_relevant_info(json_response))		
				
