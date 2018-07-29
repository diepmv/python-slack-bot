from rtmbot import RtmBot
import yaml
from config import rtmbot_config

slack_client = RtmBot(rtmbot_config).slack_client
