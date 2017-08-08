import tweepy


def getConfig():
   import json
   config = json.loads(open("config.json").read())
   return config


def getHashtag():
  hashtag = input("Enter a hashtag to create a predictive database with: ")
  return hashtag.replace("#", "")


def getTweets()
  hashtag = getHashtag()
  
 
def getNgrams():
  pass


def savePredictionData():
    pass
  

  
