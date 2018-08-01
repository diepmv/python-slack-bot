from rtmbot import RtmBot
from argparse import ArgumentParser
import sys
import os
from config import rtmbot_config
import logging


#sys.path.append(os.path.normpath(os.getcwd() + os.sep + os.pardir))
# sys.path.append(os.getcwd())
#os.chdir(os.getcwd() + os.sep + os.pardir))

def main():
    logging.basicConfig(filename='slackbot.log', level=logging.DEBUG)
    logger = logging.getLogger()

    bot = RtmBot(rtmbot_config)
    try:
        bot.start()
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        logger.error('Error when run bot', exc_info=True)


if __name__=="__main__":
    main()
