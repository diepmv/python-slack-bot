from rtmbot.core import Plugin, Job
from clients.slack import User

class myJob(Job):

	def run(self, slack_client):
		user = User('UBYCDR9B6')
		userChannel = user.get_user_channel(slack_client)

		slack_client.api_call(
				"chat.postMessage",
				channel=userChannel,
				text='Hello from Python! :tada:", icon_emoji=":robot_face:', 
				as_user=True
			)


		return [["#general", "hello world"]]



class MyPlugin(Plugin):

	def register_jobs(self):
		job = myJob(5)
		self.jobs.append(job)