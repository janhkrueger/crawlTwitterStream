SELECT tweetid, tweetcontent -> 'text' as tweet
FROM twitter.tweets
WHERE tweetcontent -> 'entities' -> 'hashtags' @> '[{"text":"evede"}]'
ORDER BY tweetid ASC
