# Tweet Timeout
Script that removes tweets older than 90 days.  

### Motivation
Protect yourself from  mining of old tweets which could be used:

- in a social engineering attack
- by advertisers
- to embarrass you

Be nice on Twitter!

### How it works
TweetTimeout connects to your account, either private or public with the token credentials that you provide (see below).  

The script then reads the creation date on all tweets and compares against the current date minus 90 days.  

The tweets older than 90 days are permanently deleted.

### Usage
For best results run on a Raspberry Pi using [crontab](https://www.howtogeek.com/101288/how-to-schedule-tasks-on-linux-an-introduction-to-crontab-files/)  set run once a day.
#### Dependencies
- Python 2.7
- [tweepy](https://github.com/tweepy/tweepy)
- A Twitter [access token](https://developer.twitter.com/en/docs/accounts-and-users/subscribe-account-activity/guides/getting-started-with-webhooks) 

#### Credentials

Once the access tokens are created, put them in the appropriate spots in the account.json file. 
 
Copy and rename this file if using multiple accounts.  

	{
	    "consumer_key": "place consumer key here",
	    "consumer_secret": "place consumer secret here",
	    "access_token": "place access here",
	    "access_secret": "place access secret here"
	}

#### Execution Instructions

Run the TweetTimeout.py with the account.json as a command line argument

If there are many tweets overdue, the script may take awhile to delete everything.

	$ python TweetTimeout.py account.json

The script will output either pass or destroyed.
