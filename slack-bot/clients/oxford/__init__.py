import requests
import config

url = "https://od-api.oxforddictionaries.com/api/v1/entries/en/cat"


class OxfordDictionary():
	def __init__(self):
		self.app_id = config.APP_ID
		self.app_key = config.APP_KEY
		self.base_url = config.Oxford_API_Base_URL

	def get_definition(self, word):
		url = self.base_url + "/entries/en/{word_id}".format(word_id=word)
		headers = {'app_id': self.app_id, 'app_key':self.app_key}
		r = requests.get(url, headers=headers)
		print(r.json())
		return r.json()