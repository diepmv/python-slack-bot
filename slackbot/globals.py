from rtmbot import RtmBot
import yaml
from config import rtmbot_config
from clients.sentry import create_client


slack_client = RtmBot(rtmbot_config).slack_client
sentry_client = create_client()