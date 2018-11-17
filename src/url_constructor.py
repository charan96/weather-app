import re

class URLConstructor:
	def __init__(self, apikey, country_code=None):
		self.apikey = apikey
		self.country_code = "us" if country_code is None else country_code

		self.base_url = "http://api.openweathermap.org/data/2.5/weather?zip="

	@staticmethod
	def is_valid_zipcode(zipcode):
		regex = re.compile(r'\d{5}')
		
		if regex.match(zipcode):
			return zipcode
		else:
			raise ValueError('invalid zip code; must be only 5 digits for US zipcodes')

	def assemble_url(self, zipcode):
		""" assembles URL in this format: 
		    api.openweathermap.org/data/2.5/weather?zip={zip code},{country code}&APPID={} 
		"""
		return self.base_url + zipcode + ',' + self.country_code + '&APPID=' + self.apikey

	def generate_url(self, zipcode):
		if URLConstructor.is_valid_zipcode(zipcode):
			return self.assemble_url(zipcode)

