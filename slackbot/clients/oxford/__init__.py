import requests
from config import config


class OxfordDictionary(object):
	def __init__(self):
		print(config)
		self.app_id = config.get('DEFAULT', 'app_id')
		self.app_key = config.get('DEFAULT', 'app_key')
		self.base_url = config.get('DEFAULT', 'oxford_api_base_url')
		

	def get_definition(self, word):
		url = self.base_url + "/entries/en/{word_id}".format(word_id=word)
		headers = {'app_id': self.app_id, 'app_key':self.app_key}
		try:
			r = requests.get(url, headers=headers)
			print(r,5555555555)
		except Exception as e:
			print(e)
		print(r.json())
		return r.json()