import tweepy, time, sys

CONSUMER_KEY = '#########'
CONSUMER_SECRET = '#######'
ACCESS_KEY = '########'
ACCESS_SECRET = '########'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename=open('jeannybot.txt','r')
f=filename.readlines()
filename.close()

for line in f:
 api.update_status(status=line)
 time.sleep(900)
