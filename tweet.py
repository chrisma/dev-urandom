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
from PIL import Image

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

def generate_text():
	text = ''
	while len(text) < TWEET_LENGTH:
		# 'utf-8'? pfff...
		encoding = random.choice(ENCODINGS_LIST)
		char = os.urandom(64).decode(encoding, errors='ignore')
		text += char[0]
	logging.info(text)
	return text

def generate_image(width=256, height=256, path='image.png'):
	image = Image.new('RGB', (width, height))
	for x in range(width):
		for y in range(height):
			r = random.randint(0, 255)
			g = random.randint(0, 255)
			b = random.randint(0, 255)
			image.putpixel((x, y), (r, g, b))
	image.save(path)
	return path

def send_tweet(account, status_text, status_image_path=None):
	media_id = None
	if status_image_path:
		with open(status_image_path, 'rb') as image:
			# https://twython.readthedocs.io/en/latest/usage/advanced_usage.html#updating-status-with-image
			response = account.upload_media(media=image)
			media_id = response['media_id']
			logging.info(f"Uploaded image response: {response}")
	
	tweet = account.update_status(
		status=status_text,
		media_ids=[media_id] if media_id else []
	)
	try:
		# Gotta like this tweet. After all, we wrote it
		account.create_favorite(id=tweet['id'])
	except TwythonError as e:
		logging.info(f"Could not favorite tweet '{tweet['id']}'")
	return tweet


if __name__ == '__main__':
	logging.basicConfig(level=logging.INFO)
	logging.info('Started!')

	# randint(a, b): Return a random integer N such that a <= N <= b
	if randint(1,4) != 1:
		logging.info('Not tweeting this time.')
		sys.exit()

	logging.info('Attempting to tweet')
	account, account_info = login()
	if randint(1,10) != 1:
		text = generate_text()
		tweet = send_tweet(account, text, None)
	else:
		logging.info('Photo time!')
		image = generate_image()
		tweet = send_tweet(account, None, image)

	logging.info(f"Posted: https://twitter.com/{account_info['screen_name']}/status/{tweet['id']}")
