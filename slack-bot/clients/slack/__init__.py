
from rtmbot import RtmBot
import yaml

config = yaml.load(open('rtmbot.conf', 'r'))
bot = RtmBot(config)


class User(object):
	def __init__(self, member_id):
		self.member_id = member_id
		self.client = bot.slack_client


	def get_user_channel(self):
		userChannel = self.client.api_call(
			"im.open",
			user=self.member_id
		)
		return userChannel['channel']['id']