from globals import slack_client


class Member(object):
	def __init__(self, member_id):
		self.member_id = member_id
		self.client = slack_client


	def get_user_channel(self):
		userChannel = self.client.api_call(
			"im.open",
			user=self.member_id
		)
		return userChannel['channel']['id']