# /dev/urandom Twitter bot
A pretty random tweet-machine, manning the Twitter handle [@dev__urandom](https://twitter.com/dev__urandom).  
Tweeting the wisdom of [/dev/urandom](http://linux.die.net/man/4/urandom).  
Never out of things to say, due to the source of its inspiration.  
Either a silly idea or satire.

Runs on [OpenShift](https://www.openshift.com/).

![Screenshot](screenshot.png)

## Run the Thing
* Clone/Fork the repo
* Register an app at [https://dev.twitter.com/apps](https://dev.twitter.com/apps)
* Copy your tokens to `credentials.py`
* Ignore changes to `credentials.py`, so you don't commit your keys:
  `git update-index --assume-unchanged credentials.py`
* Run `python tweet.py`
