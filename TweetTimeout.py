import tweepy
import sys
import json
import time
import datetime

global no_unicode

# open json file containing authentication info
try:
    with open(sys.argv[1]) as data_file:
        data = json.load(data_file)
except IndexError:
    print "This script takes a command line argument"
    print "Usage: TweetTimeout.py account.json"
    sys.exit(1)

# Parse json file
consumer_key = data["consumer_key"]
consumer_secret = data["consumer_secret"]
access_token = data["access_token"]
access_secret = data["access_secret"]

#Use tweepy to authenicate user
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

# Current time delta 90 days ago
time_delta = datetime.datetime.now() + datetime.timedelta(-90)

# Loop though each Cursor page to get all tweets
for tweet in tweepy.Cursor(api.user_timeline).items():
    
    # Created at object from tweet object
    tweet_time = tweet.created_at
    
    # Check if the tweet is older than 90 days
    if tweet_time < time_delta:
        try:
            # destory status with id
            api.destroy_status(tweet.id)
        except:
            print "Delete tweet exception"

# Loop through likes
for tweet in tweepy.Cursor(api.favorites).items():
    
    tweet_time = tweet.created_at

    # Check if the tweet is older than 90 days
    if tweet_time < time_delta:
        try:
            # destory status with id
            api.destroy_favorite(tweet.id)
        except:
            print "Delete likes exception"
