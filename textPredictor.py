def getConfig():
  import json
  config = json.loads(open("config.json").read())
  return config


def weightedRandomByDict(dct):
  import random
  randVal = random.random() * sum(list(dct.keys()))
  total = 0
  for key, value in dct.items():
    total += value
    if ranValue <= total:
      return key
  assert False, 'unreachable'
    
    
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
        prediction = tweet[index:].split()[:predictionLength - 1]
        if prediction in predictions:
          predictions[prediction] += 1
        else:
          predictions[prediction] = 1
  prediction = " ".join(weightedRandomByDict(predictions))
  return prediction
  
def predictionLoop():
  tweets = getTweets()
  print("Press control-C to escape loop")
  while True:     
    text = input("Enter some text: ")
    prediction = makePrediction(text, tweets)
    print(text + " " prediction)

    
predictionLoop()
