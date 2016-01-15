#!/usr/bin/env python

from twython import Twython
from credentials import *
from os import urandom

def random_tweet(account):
	# https://docs.python.org/2/library/codecs.html
	status = urandom(400).decode('utf-8', errors='ignore')
	status = status[0:140]
	tweet = account.update_status(status=status)
	# Gotta like this tweet, after all, we wrote it
	account.create_favorite(id=tweet['id'])

if __name__ == '__main__':
	account = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
	random_tweet(account)
