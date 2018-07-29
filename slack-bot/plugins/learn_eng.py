from rtmbot.core import Plugin, Job
from clients.slack import User
from clients.oxford import OxfordDictionary


class myJob(Job):

	def run(self, slack_client):
		userChannel = User('UBYCDR9B6').get_user_channel()
		print 22
		slack_client.api_call(
				"chat.postMessage",
				channel=userChannel,
				text=OxfordDictionary().get_definition('cat'), 
				as_user=True
			)


		return [["#general", "hello world"]]


class MyPlugin(Plugin):

	def register_jobs(self):
		job = myJob(5)
		self.jobs.append(job)