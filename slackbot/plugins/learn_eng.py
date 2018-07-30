from rtmbot.core import Plugin, Job
from clients.slack import Member
from clients.oxford import OxfordDictionary


class myJob(Job):

	def run(self, slack_client):
		member = Member('UBYCDR9B6')
		direct_channel_id = member.get_direct_channel_id()

		slack_client.api_call(
				"chat.postMessage",
				channel=direct_channel_id,
				text=OxfordDictionary().get_definition('cat'), 
				as_user=True
			)


		return [["#general", "hello world"]]


class MyPlugin(Plugin):

	def register_jobs(self):
		job = myJob(5)
		self.jobs.append(job)