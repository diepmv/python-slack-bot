import ConfigParser
import yaml

config = ConfigParser.ConfigParser()
config.read('config.ini')


rtmbot_config = yaml.load(open('rtmbot.conf', 'r'))