import unittest
import tweepy
import requests
import json
import twitter_info


consumer_key = twitter_info.consumer_key
consumer_secret = twitter_info.consumer_secret
access_token = twitter_info.access_token
access_token_secret = twitter_info.access_token_secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

TW_CACHE="cache_user_info.json"
# TW_DICTION = {}
try: 
	cache_file=open(TW_CACHE,"r")
	cache_contents=cache_file.read()
	TW_DICTION=json.loads(cache_contents)
except:
	TW_DICTION={}

a=input("type in a keyword")
def user_tweets(a):
	unique_id="{}".format(a)
	if unique_id in TW_DICTION:
		results=TW_DICTION[unique_id]
	else:
		results=api.search(q="{}".format(a))
		TW_DICTION[unique_id]=results
		f=open(TW_CACHE,"w")
		f.write(json.dumps(TW_DICTION))	
		f.close()
	tw=results["statuses"]
	for items in tw[0:3]:
		print (items["text"])
		print (items["created_at"])
		print ("\n")

print(user_tweets(a))





# look_up_tweet=api.search(q="{}".format(a))