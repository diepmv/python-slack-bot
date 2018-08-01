import ConfigParser
import yaml

config = ConfigParser.ConfigParser()
config.read('config.ini')


rtmbot_config = yaml.load(open('rtmbot.conf', 'r'))

_configDict = { 
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': { 
        'standard': { 
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },'test': {
        	'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        }
    },
    'handlers': { 
        'default': { 
            'level': 'INFO',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
        },'test': {
        	'level': 'DEBUG',
        	'formatter': 'test'
        }
    },
    'loggers': { 
        '': { 
            'handlers': ['default'],
            'level': 'INFO',
            'propagate': True
        },
        'slackbot': { 
            'handlers': ['test'],
            'level': 'WARN',
            'propagate': False
        },
    } 
}

logging.config.dictConfig(_configDict)