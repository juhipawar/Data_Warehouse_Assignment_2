

#  Sentiment Analysis of Twitter Tweet Data using ETL Process and Elastic Search



### Instructions


1. Install Python3
```
python3 -V
```
2. Install pip package manager
```
sudoapt-get install -y python3-pip
```
3. Install tweepy
```
pip3 install tweepy
```
4. Create Twitter Account and App. This will give access to the credentials such as Customer key, Customer Secret key, Access Token and Access Token Secret.

![alt text](https://github.com/juhipawar/Data_Warehouse_Assignment_2/blob/master/d1.png)

5. Create a sample Python App on the instance created on AWS.
6. Import Tweepy
7. Copy the Twitter App credentials
```
consumer_key= "FC1...uM"
consumer_secret= "lLXBeSY...MevLJ5g"
access_key= "28419...oh04R"
access_secret= "6QcxzJR...UalxSlg"
```
8.Establish the connection using OAuth
```
auth= tweepy.OAuthHandler(consumer_key, consumer_secret)auth.set_access_token(access_key, access_secret)api= tweepy.API(auth)
```
9.Get Data from profile
```
def get_profile(screen_name):
    api= tweepy.API(auth)
    try:
     user_profile = api.get_user(screen_name)
   except tweepy.error.TweepErroras e:
     user_profile = json.loads(e.response.text)
    return user_profile
```
10.Get Trending Topics
```
def get_trends(location_id):
   tweepyapi = tweepy.API(auth)
   try:
      trends = api.trends_place(location_id)
   except tweepy.error.TweepError as e:
      trends = json.loads(e.response.text)

   return trends
```
11.Standard Search Query
```
def get_tweets(query):
    api = tweepy.API(auth)
    try:
       tweets = api.search(query)
    except tweepy.error.TweepError as e:
       tweets = [json.loads(e.response.text)]

    return tweets
```

![alt text](https://github.com/juhipawar/Data_Warehouse_Assignment_2/blob/master/d2%20(2).png)

12. Clean the tweets and save into CSV.
```
queries = ["#GlobalRunningDay -filter:retweets lang:en","#AStarIsBorn -filter:retweets lang:en","#DDay -filter:retweets lang:en","#SunilChhetri -filter:retw$
with open ('Clean_file.csv','w') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['id', 'user', 'created_at', 'text'])
        for query in queries:
                t = get_tweets(query)
                for tweet in t:
                        tweet.text=' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",tweet.text).split())
                        writer.writerow([tweet.id_str,tweet.user.screen_name,tweet.created_at,tweet.text])
```
![alt text](https://github.com/juhipawar/Data_Warehouse_Assignment_2/blob/master/d8.png)

![alt text](https://github.com/juhipawar/Data_Warehouse_Assignment_2/blob/master/d10.png)

13. Sentiment Analysis 
```
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
    print("{:-<65} {}".format(row[3], str(readTweets)))
    positive = readTweets['pos']
    negative = readTweets['neg']
    neutral = readTweets['neu']
    arr = np.array([positive,negative,neutral])
    index = np.argmax(arr)
    if index==0:
        sentiments.append('positive')
    elif index==1:
        sentiments.append('negative')
    elif index==2:
        sentiments.append('neutral')
    scores.append(np.max(arr))
    tweets.append(row[3])
dataFrame['tweet'] = tweets
dataFrame['sentiment'] = sentiments
dataFrame['sentiment_score'] = scores
dataFrame.to_csv('File_sentimental.csv',index=False)

```

![alt text](https://github.com/juhipawar/Data_Warehouse_Assignment_2/blob/master/D89.png)

![alt text](https://github.com/juhipawar/Data_Warehouse_Assignment_2/blob/master/d90.png)

14. Loading data into Elastic Search DB
```
```
15. ETL as Batch Process
* Create file named shellscript.sh
* Type the text in this file as shown in figure below.

![alt text](https://github.com/juhipawar/Data_Warehouse_Assignment_2/blob/master/d91.png)

* Type the command 'chmod u+x shellscript.sh'
* Run the file by using the command './shellscript.sh'

![alt text](https://github.com/juhipawar/Data_Warehouse_Assignment_2/blob/master/d34.png)
















  



















   

   
