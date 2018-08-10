import json
from textblob import TextBlob
import matplotlib.pyplot as plt

#get json tweet data from tweets.json - convert it so python can use it
tweerFile = open("tweets.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

#Textblob sample (you won't need this in your final file):
tb = TextBlob("You are a brilliant computer scientist.")
print(tb.polarity)

#Create a list to hold polarity values for each tweet
    ###your list here###

#Get sentiment data: add polarities into list
for tweet in tweetData:
        ###your code here####Print out polarity values
