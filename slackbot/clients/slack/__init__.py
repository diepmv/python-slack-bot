from globals import slack_client


def list_all_member():
	return slack_client.api_call("users.list")['members']



class Member(object):
	'''
	The member slack object to get information about member like 
	user_channel_id
	'''
	client = slack_client
	__slots__ = ['member_id']
	
	def __init__(self, member_id):
		self.member_id = member_id

	# get id of direct channel
	def get_direct_channel_id(self):
		direct_message = self.client.api_call("im.open", user=self.member_id)
		channel_id = direct_message['channel']['id']
		return channel_id

	def get_email(self):
		for member in list_all_member():
			if member['id'] == self.member_id:
				return member['profile'].get('email')

	@classmethod
	def from_email(cls, email): # alternative constructor anticipate subclassing
		member_id = get_id_from_email(email)
		return cls(member_id)

	@staticmethod
	def get_id_from_email(email):
		all_members = list_all_member
		for mem in all_members:
			if mem['profile'].get('email') == email:
				return member['id']

	# Todo: get member name, display name