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
  except: #might want to check this is not an eror ^^
    print("No tweet database for this hashtag :/")
    sys.exit()

def continuousPredictor():
  print("Press control-C to escape loop")
  while True:
    pass
