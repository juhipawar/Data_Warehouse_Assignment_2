from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer # Adpeted from https://github.com/cjhutto/vaderSentiment
import csv
import numpy as np
import pandas as pd

inputFile = open('Clean_file.csv')
fileObject= csv.reader(inputFile)

sentimentIntensityAnalyzer = SentimentIntensityAnalyzer()
dataFrame = pd.DataFrame(columns=['tweets','sentiments','scores'])
scores = []
sentiments = []
tweets = []
for index,row in enumerate(fileObject):
    readTweets = sentimentIntensityAnalyzer.polarity_scores(row[3])
    positive = readTweets['pos']
    negative = readTweets['neg']
    neutral = readTweets['neu']
    npArray = np.array([positive,negative,neutral])
    index = np.argmax(npArray)
    def switch_demo(index):
        swticher = {
            0: positive,
            1: negative,
            2: neutral
        } 
        sentiments.append(index)
    scores.append(np.max(npArray))
    tweets.append(row[3])
dataFrame['tweet'] = tweets
dataFrame['sentiment'] = sentiments
dataFrame['sentiment_score'] = scores
dataFrame.to_csv('File_sentimental.csv',index=False)
