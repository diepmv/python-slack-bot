import requests
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('config.ini')


class OxfordDictionary():
	def __init__(self):
		self.app_id = config['DEFAULT']['APP_ID']
		self.app_key = config['DEFAULT']['APP_KEY']
		self.base_url = config['DEFAULT']['Oxford_API_Base_URL']

	def get_definition(self, word):
		url = self.base_url + "/entries/en/{word_id}".format(word_id=word)
		headers = {'app_id': self.app_id, 'app_key':self.app_key}
		r = requests.get(url, headers=headers)
		print(r.json())
		return r.json()