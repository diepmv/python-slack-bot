#!/usr/bin/env python

from setuptools import setup, find_packages
import os
import slackbot


def extra_dependencies():
    import sys
    ret = []
    # if sys.version_info < (2, 7):
    #     ret.append('argparse')
    return ret


def read(*names):
    values = dict()
    extensions = ['.txt', '.rst']
    for name in names:
        value = ''
        for extension in extensions:
            filename = name + extension
            if os.path.isfile(filename):
                value = open(name + extension).read()
                break
        values[name] = value
    return values

long_description = """
%(README)s

News
====

%(CHANGES)s

""" % read('README', 'CHANGES')

setup(
    name='slackbot',
    version=slackbot.__version__,
    description='Slack bot real time',
    long_description=long_description,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Documentation",
    ],
    keywords='bot slack console',
    author='Mai Diep',
    author_email='diepmv@vccloud.vn',
    maintainer='Mai Diep',
    maintainer_email='diepmv@vccloud.vn',
    url='https://github.com/diepmv/python-slack-bot',
    license='MIT',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'slackbot = slackbot.__main__:main',
        ]
    },
    install_requires=[
        'certifi==2018.4.16',
        'chardet==3.0.4',
        'idna==2.7',
        'PyYAML==3.13',
        'requests==2.19.1',
        'rtmbot==0.4.1',
        'six==1.11.0',
        'slackclient==1.2.1',
        'urllib3==1.23',
        'websocket-client==0.48.0',
    ] + extra_dependencies(),
)
