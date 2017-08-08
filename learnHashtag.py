def getConfig():
  import json
  config = json.loads(open("config.json").read())
  return config


def removeText(text, term="https?://[^\s]+"):
   import re
   term = "(?P<text>" + term + ")"
   while True:
      textToRemove = re.search(term, text)
      if textToRemove:
         text = text.replace(textToRemove.group("text"), "").replace("  ", " ") 
      else: break
   return text


def getHashtag():
  hashtag = input("Enter a hashtag to create a predictive database with: ")
  return hashtag.replace("#", "")


def stripAllEntities(text):
  import string
  entity_prefixes = ['@','#']
  for separator in  string.punctuation:
    if separator not in entity_prefixes :
      text = text.replace(separator,' ')
  words = []
  for word in text.split():
    word = word.strip()
    if word:
      if word[0] not in entity_prefixes:
        words.append(word)
  return ' '.join(words)


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
    tweetText = stripAllEntities(tweetText)
    tweetText = "".join([item for item in list(tweetText) if item not in list(string.punctuation.replace("'", "") + "#!()-$@/?")])
    tweets.append(tweetText)
  return [hashtag, tweets]


def saveTweets():
  import json
  import os
  hashtag, tweets = getTweets()
  if not os.path.exists("./hashtagTweets"):
    os.makedirs("./hashtagTweets")
  print("Tweet count: " + str(len(tweets)))
  outputJson = json.dumps(tweets)
  with open("./hashtagTweets/" + hashtag + "Tweets.json", "w") as outputFile:
    outputFile.write(outputJson)
  
if __name__ == "__main__":
  saveTweets()
