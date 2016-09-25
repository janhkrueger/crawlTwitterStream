SELECT tweetid, tweetcontent -> 'text' as tweet
FROM twitter.tweets
WHERE tweetcontent -> 'user' -> 'screen_name' = '"janhkrueger"'
ORDER BY tweetid ASC
