#!/usr/bin/env python

from twython import Twython
from credentials import *
from encodings_list import *
from os import urandom
from random import randint
import random
import logging

TWEET_LENGTH = 140

def generate_content():
	# 'utf-8'? pfff.....
	text = ''
	while len(text) < TWEET_LENGTH:
		encoding = random.choice(ENCODINGS_LIST)
		logging.debug('Using encoding: "%s".' % encoding)
		char = urandom(64).decode(encoding, errors='ignore')
		text += char[0]
	logging.debug('Length: %s' % len(text))
	return text

def tweet(account, status):
	tweet = account.update_status(status=status)
	# Gotta like this tweet, after all, we wrote it
	account.create_favorite(id=tweet['id'])

if __name__ == '__main__':
	logging.basicConfig(level=logging.INFO)
	logging.debug('Started!')
	account = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

	if randint(1,150) == 1:
		status = generate_content()
		logging.debug(status)
		tweet(account, status)
	else:
		logging.debug('Not tweeting this time.')
