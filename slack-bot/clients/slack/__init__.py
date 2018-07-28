

class User(object):
	def __init__(self, member_id):
		self.member_id = member_id

	def get_user_channel(self, client):
		userChannel = client.api_call(
			"im.open",
			user=self.member_id
		)
		return userChannel['channel']['id']