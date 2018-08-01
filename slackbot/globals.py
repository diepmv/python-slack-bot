from rtmbot import RtmBot
import yaml
from config import rtmbot_config
from clients.sentry import create_client
import logging
from raven.handlers.logging import SentryHandler
from raven.conf import setup_logging

slack_client = RtmBot(rtmbot_config).slack_client
sentry_client = create_client()



# Manually specify a client

_handler = SentryHandler(sentry_client)


_handler.setLevel(logging.ERROR)



setup_logging(_handler)
