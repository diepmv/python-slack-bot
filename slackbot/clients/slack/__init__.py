from globals import slack_client


class Member(object):
	'''
	The member slack object to get information about member like 
	user_channel_id
	'''
	client = slack_client
	
	def __init__(self, member_id):
		self.member_id = member_id


	def get_user_channel(self):
		userChannel = self.client.api_call(
			"im.open",
			user=self.member_id
		)
		return userChannel['channel']['id']