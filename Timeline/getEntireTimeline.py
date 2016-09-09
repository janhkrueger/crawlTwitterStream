from twython import Twython # pip install twython
import time # standard lib
import sys, StringIO, os, json

''' Go to https://apps.twitter.com/ to register your app to get your api keys '''
CONSUMER_KEY = '' 
CONSUMER_SECRET = '' 
ACCESS_KEY = '' 
ACCESS_SECRET = ''

twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
lis = [974224843013324800] ## this is the latest starting tweet id
for i in range(0, 16): ## iterate through all tweets
## tweet extract method with the last list item as the max_id
  user_timeline = twitter.get_user_timeline(screen_name="",
  count=200, include_retweets=True, max_id=lis[-1])
  
  time.sleep(300) ## 5 minute rest between api calls

  for tweet in user_timeline:
    filename = '%s.txt' % tweet['id']
    with open( filename, 'w' ) as outfile:
      json.dump(tweet, outfile)
      outfile.closed
    lis.append(tweet['id']) ## append tweet id's
