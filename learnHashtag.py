import tweepy


def getConfig():
  import json
  config = json.loads(open("config.json").read())
  return config


def getHashtag():
  hashtag = input("Enter a hashtag to create a predictive database with: ")
  return hashtag.replace("#", "")


def initTwitterApi():
  config = getConfig()
  import tweepy
  twitterKeys = config["twitterKeys"]
  auth = tweepy.OAuthHandler(twitterKeys[0], twitterKeys[1])
  auth.set_access_token(twitterKeys[2], twitterKeys[3])
  return tweepy.API(auth, wait_on_rate_limit_notify=True, wait_on_rate_limit=True)


def getTweets():
  import tweepy
  import string
  tweets = []
  config = getConfig()
  api = initTwitterApi()
  hashtag = getHashtag()
  tweetCount = config["tweetCount"]
  search = tweepy.Cursor(api.search, q="#" + hashtag, tweet_mode="extended", lang="en")
  for tweet in search.items(tweetCount):
    tweetText = removeText(tweet._json["full_text"]).lower().strip()
    tweetText = "".join([item for item in list(tweetText) if item not in list(string.punctuation + "#!()-$@/'?")])
    tweets.append(tweetText)
  return tweetText

 
def getNgrams():
  pass


def savePredictionData():
  pass
  

  
