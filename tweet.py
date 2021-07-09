#!/usr/bin/env python

from twython import Twython
from twython.exceptions import TwythonError
from credentials import *
from encodings_list import ENCODINGS_LIST
from random import randint
import os
import sys
import random
import logging

TWEET_LENGTH = 140

def login():
	# Get credentials from credentialy.py, fall back to env variables (used in GH Actions workflow)
	account = Twython(
		os.environ.get('API_KEY') or API_KEY,
		os.environ.get('API_SECRET_KEY') or API_SECRET_KEY,
		os.environ.get('ACCESS_TOKEN') or ACCESS_TOKEN,
		os.environ.get('ACCESS_TOKEN_SECRET') or ACCESS_TOKEN_SECRET)
	info = account.verify_credentials()
	logging.info(f"Logged in as '{info['name']}' (@{info['screen_name']}). Tweets: {info['statuses_count']}, Followers: {info['followers_count']}")
	return account, info

def generate_content():
	# 'utf-8'? pfff...
	text = ''
	while len(text) < TWEET_LENGTH:
		encoding = random.choice(ENCODINGS_LIST)
		char = os.urandom(64).decode(encoding, errors='ignore')
		text += char[0]
	logging.info(text)
	return text

def send_tweet(account, status):
	tweet = account.update_status(status=status)
	try:
		# Gotta like this tweet. After all, we wrote it
		account.create_favorite(id=tweet['id'])
	except TwythonError as e:
		logging.info(f"Could not favorite tweet '{tweet['id']}'")
	return tweet


if __name__ == '__main__':
	logging.basicConfig(level=logging.INFO)
	logging.info('Started!')

	if randint(1,4) != 1:
		logging.info('Not tweeting this time.')
		sys.exit()

	logging.info('Attempting to tweet')
	account, account_info = login()
	text = generate_content()
	tweet = send_tweet(account, text)
	logging.info(f"Posted: https://twitter.com/{account_info['screen_name']}/status/{tweet['id']}")
