import tweepy
import wget

import twitter_credentials

auth = tweepy.OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)


def download_image(hashtag):
    api = tweepy.API(auth)
    media_files = set()
    filesname = []
    public_tweets = api.search(hashtag, count=2)
    filename = ""
    for tweet in public_tweets:
        print tweet.text
        media = tweet.entities.get("media",[])
        if(len(media) > 0):
            media_files.add(media[0]["media_url"])

    for media_file in media_files:
        filesname.append(wget.download(media_file))

    return filesname
