from rtmbot import RtmBot
from argparse import ArgumentParser
import sys
import os
from config import rtmbot_config


sys.path.append(os.path.normpath(os.getcwd() + os.sep + os.pardir))

def main():
    bot = RtmBot(rtmbot_config)
    print bot, 111
    try:
        bot.start()
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
    	print(333)
    	print(e, 111)


if __name__=="__main__":
    main()