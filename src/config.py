import json

class Config:
	def __init__(self, filename):
		self.filename = filename
		self.apikey = self.load_config()
	
	def load_config(self):
		with open(self.filename, 'r') as fh:
			data = json.load(fh)
			return data['apikey']

	def get_api_key(self):
		return self.apikey

