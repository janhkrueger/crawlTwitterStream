# crawlTwitterStream
Basic set to save all Tweets of a specific hashtag as json

=============
### Technologies including this project:
- Python 2.7.9
- PostgreSQL 9.4.9
- [Tweepy-API][1]

=============
### Contents
- run.py: uses the Streaming API to get all tweets, filtered my hashtags definied in the config file config.json
- saveTweets.py: fetches all tweetfiles and stores them in a PostgreSQL database
- createDB.sql: creates the table to store the tweets
- config.json: central configuration file. Twitter credentials and hashtag filter
- sampleTweet.txt: a sample tweet
- exportTweets.py: if tweets are needet as textfiles sometimes later, exorts them as [tweetid].txt

=============
### Starting the crawler 
Starting is easy. Just type the following:

```
python run.py --client=config.json
```

I prefer setting up a cronjob for it. To ensure that only one instance is running, there is a little wrapper, working with a lock file: __loadTweetsWrapper.sh__

In the current directory the crawler saves every tweet as a textfile, named like: _[tweetID]_.txt. Sample: __774224843013324800.txt__

=============
### Storing the tweets in the database 
```
python saveTweets.py
```

Looks for *.txt files and tries to store the json data in the table in a JSONB datatype. If successfull, deletes the file.

=============
### Exporting tweets from the database 
For testing purposes you can export tweets stored ni the database. They are saved as simple textfiles, named like _[tweetID]_.txt 
Just run:

```
python exportTweets.py
```


[1]: https://github.com/tweepy/tweepy
