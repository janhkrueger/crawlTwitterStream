-- Table structure for storing the tweets
CREATE TABLE twitter.tweets (
  tweetid int8 NOT NULL,
  tweetcontent jsonb,
  PRIMARY KEY (tweetid)
) WITH (OIDS=FALSE);


-- some Index on the jsonb datatype
DROP INDEX idx_tweets_language;
CREATE INDEX idx_tweets_language 
ON twitter.tweets ((tweetcontent->>'lang'));

DROP INDEX idx_tweets_writer;
CREATE INDEX idx_tweets_writer 
ON twitter.tweets ((tweetcontent->>'screen_name'));

DROP INDEX idx_tweets_timestamp;
CREATE INDEX idx_tweets_timestamp 
ON twitter.tweets ((tweetcontent->>'timestamp_ms'));

DROP INDEX idx_tweets_placetype;
CREATE INDEX idx_tweets_placetype 
ON twitter.tweets ((tweets.tweetcontent->'place'->>'place_type'));

DROP INDEX idx_tweets_placecountry;
CREATE INDEX idx_tweets_placecountry 
ON twitter.tweets ((tweets.tweetcontent->'place'->>'country'));
