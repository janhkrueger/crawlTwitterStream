SELECT tweets.tweetcontent -> 'id' AS tweetid,
    tweets.tweetcontent -> 'place' ->> 'country_code' AS country,
    tweets.tweetcontent -> 'place' AS place,
    tweets.tweetcontent -> 'text' AS inhalt
   FROM tweets
  WHERE tweets.tweetcontent -> 'place' ->> 'country_code' != 'NULL'
  ORDER BY tweets.tweetcontent -> 'place' ->> 'id', tweets.tweetcontent -> 'user' ->> 'screen_name';
