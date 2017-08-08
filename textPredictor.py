def getConfig():
  import json
  config = json.loads(open("config.json").read())
  return config


def getHashtag():
  import json
  hashtag = input("Enter a hashtag to base predictions off: ").replace("#", "")
  return hashtag


def getTweets():
  import json
  import sys
  hashtag = getHashtag()
  try:
    tweets = json.loads(open(hashtag + "Tweets.json").read())
  except: 
    print("No tweet database for this hashtag :/")
    sys.exit()
  return tweets

    
def makePrediction(text, tweets):
  import re
  config = getConfig()
  predictions = {}
  predictionDepth = config["predictionDepth"]
  predictionLength = config["predictionLength"]
  predictionBase = text.split()[-predictionDepth:]
  for tweet in tweets:
    if predictionBase in tweet:
      indexes = [m.start() + len(predictionBase) for m in re.finditer(predictionBase, tweet)]
      for index in index:
        prediction = tweet[index:].split()[:2]
     
  
def predictionLoop():
  tweets = getTweets()
  print("Press control-C to escape loop")
  while True:     
    pass
