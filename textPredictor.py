def getConfig():
  import json
  config = json.loads(open("config.json").read())
  return config


def weightedRandomByDict(dct):
  import random
  randValue = random.random() * sum(list(dct.values()))
  total = 0
  for key, value in dct.items():
    total += value
    if randValue <= total:
      return key
  return ""
    
    
def getHashtag():
  import json
  hashtag = input("Enter a hashtag to base predictions off: ").replace("#", "")
  return hashtag


def getTweets():
  import json
  import sys
  hashtag = getHashtag()
  try:
    tweets = json.loads(open("./hashtagTweets/" + hashtag + "Tweets.json").read())
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
  predictionBase = " ".join(text.split()[-predictionDepth:])
  for tweet in tweets:
    if predictionBase in tweet:
      indexes = [m.start() + len(predictionBase) for m in re.finditer(predictionBase, tweet)]
      for index in indexes:
        prediction = " ".join(tweet[index:].split()[:predictionLength])
        if not prediction.startswith(" "):
          prediction = " " + prediction if tweet[index:].startswith(" ") else prediction
        if prediction in predictions:
          predictions[prediction] += 1
        else:
          predictions[prediction] = 1
  prediction = weightedRandomByDict(predictions)
  return prediction
  
  
def predictionLoop():
  import sys
  tweets = getTweets()
  print("Press ctrl-C to escape loop")
  try:
    while True:     
     text = input("Enter some text: ").lower()
     prediction = makePrediction(text, tweets)
     print(text + prediction)
  except KeyboardInterrupt:
    print()
    sys.exit()

if __name__ == "__main__": 
  predictionLoop()
