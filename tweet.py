#!/usr/bin/env python

from twython import Twython
from credentials import *
from encodings_list import *
from random import randint
import os
import sys
import random
import logging

TWEET_LENGTH = 140

def generate_content():
	# 'utf-8'? pfff...
	text = ''
	while len(text) < TWEET_LENGTH:
		encoding = random.choice(ENCODINGS_LIST)
		logging.info(f"Using encoding: '{encoding}'")
		char = os.urandom(64).decode(encoding, errors='ignore')
		text += char[0]
	logging.info(f"Status length: {len(text)}")
	return text

def tweet(account, status):
	tweet = account.update_status(status=status)
	# Gotta like this tweet, after all, we wrote it
	account.create_favorite(id=tweet['id'])

if __name__ == '__main__':
	logging.basicConfig(level=logging.INFO)
	logging.info('Started!')

	if randint(1,4) != 1:
		logging.info('Not tweeting this time.')
		sys.exit()

	logging.info('Attempting to tweet')
	# Get credentials from credentialy.py, fall back to env variables (used in GH Actions workflow)
	account = Twython(
		os.environ.get('API_KEY') or API_KEY,
		os.environ.get('API_SECRET_KEY') or API_SECRET_KEY,
		os.environ.get('ACCESS_TOKEN') or ACCESS_TOKEN,
		os.environ.get('ACCESS_TOKEN_SECRET') or ACCESS_TOKEN_SECRET)
	info = account.verify_credentials()
	logging.info(f"Logged in as '{info['name']}' (@{info['screen_name']}). Tweets: {info['statuses_count']}, Followers: {info['followers_count']}")

	status = generate_content()
	logging.info(status)
	tweet(account, status)
