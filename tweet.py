#!/usr/bin/env python

from twython import Twython
from credentials import *
from encodings_list import *
from random import randint
import os
import random
import logging

TWEET_LENGTH = 140

def generate_content():
	# 'utf-8'? pfff...
	text = ''
	while len(text) < TWEET_LENGTH:
		encoding = random.choice(ENCODINGS_LIST)
		logging.debug(f"Using encoding: '{encoding}'")
		char = os.urandom(64).decode(encoding, errors='ignore')
		text += char[0]
	logging.debug(f"Status length: {len(text)}")
	return text

def tweet(account, status):
	tweet = account.update_status(status=status)
	# Gotta like this tweet, after all, we wrote it
	account.create_favorite(id=tweet['id'])

if __name__ == '__main__':
	logging.basicConfig(level=logging.DEBUG)
	logging.debug('Started!')
	# Get credentials from credentialy.py, fall back to env variables (used in GH Actions workflow)
	account = Twython(
		API_KEY or os.environ['API_KEY'],
		API_SECRET_KEY or os.environ['API_SECRET_KEY'],
		ACCESS_TOKEN or os.environ['ACCESS_TOKEN'],
		ACCESS_TOKEN_SECRET or os.environ['ACCESS_TOKEN_SECRET'])
	info = account.verify_credentials()
	logging.debug(f"Logged in as '{info['name']}' (@{info['screen_name']}). Tweets: {info['statuses_count']}, Followers: {info['followers_count']}")

	if randint(1,4) == 1:
		status = generate_content()
		logging.debug(status)
		tweet(account, status)
	else:
		logging.debug('Not tweeting this time.')
