from rtmbot import RtmBot
from argparse import ArgumentParser
import sys
import os
import yaml

sys.path.append(os.getcwd())


def main():
    config = yaml.load(open('rtmbot.conf', 'r'))
    bot = RtmBot(config)

    try:
        bot.start()
    except KeyboardInterrupt:
        sys.exit(0)

if __name__=="__main__":
	main()