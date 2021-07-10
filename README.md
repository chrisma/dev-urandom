# /dev/urandom Twitter Bot

Tweeting the wisdom of [/dev/urandom](http://linux.die.net/man/4/urandom) at [@dev__urandom](https://twitter.com/dev__urandom).  
Never out of things to say, due to the source of its inspiration.

<img width="622" alt="image" src="https://user-images.githubusercontent.com/1652117/124941846-68a77880-e00b-11eb-957a-106e79700b82.png">

Powered by GitHub Actions.

## Run it
* Clone/Fork the repo
* Register an app at [https://developer.twitter.com/en/apps](https://developer.twitter.com/en/apps)
* Copy your generated API tokens to `credentials.py`, store them as environment variables, or store them as [GitHub repository secrets](https://docs.github.com/en/actions/reference/encrypted-secrets#creating-encrypted-secrets-for-a-repository) when using the GitHub Actions workflow.
* Ignore changes to `credentials.py`, so you don't commit your keys:
  `git update-index --assume-unchanged credentials.py`
* Run `python tweet.py` to run locally, or see the scheduled GitHub Actions runs.
