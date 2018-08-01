from raven import Client
from config import config


def create_client():
	return Client(config.get('DEFAULT', 'sentry_dsn'))