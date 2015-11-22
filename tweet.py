#!/usr/bin/env python

from twython import Twython
from credentials import *
from os import urandom

if __name__ = '__main__':
	twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

	# https://docs.python.org/2/library/codecs.html#python-specific-encodings
	status = urandom(140).decode('raw_unicode_escape')

	tweet = twitter.update_status(status=status)

	# Gotta like this tweet, after all, we wrote it
	twitter.create_favorite(id=tweet['id'])
