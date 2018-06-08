import tweepy
import time
import json
import csv
import re

consumer_key ="SFv8w97fPUPxAxDTpdMJK728w"
consumer_secret="so1My2kX77hGN1JVwDpwxN8eHOPztTM8BCT4ooIohdiVPTEBpq"
access_key = "1004036112178995203-f3PGviIQi5aicGqMmZZQ1Llp2Iw6Bj"
access_secret = "cdRtWfGHtrIbE68P6NuanTNX183TxjSkwNedqtUQKUVhg"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_key,access_secret)
api= tweepy.API(auth)

#Extracting data from the twitter account

def get_profile(screen_name):
    tweepyapi = tweepy.API(auth)
    try:
       user_profile = api.get_user(screen_name)
    except tweepy.error.TweepError as e:
      user_profile = json.loads(e.response.text)

    return user_profile

#Extracting the trending topic

def get_trends(location_id):
   tweepyapi = tweepy.API(auth)
   try:
      trends = api.trends_place(location_id)
   except tweepy.error.TweepError as e:
      trends = json.loads(e.response.text)

   return trends

#Standard Search Query

def get_tweets(query):
    api = tweepy.API(auth)
    try:
       tweets = api.search(query)
    except tweepy.error.TweepError as e:
       tweets = [json.loads(e.response.text)]

    return tweets

#Saving to CSV

queries = ["#GlobalRunningDay -filter:retweets lang:en","#AStarIsBorn -filter:retweets lang:en","#DDay -filter:retweets lang:en","#SunilChhetri -filter:retweets lang:en","#BackTheBlue -filter:retweets lang:en","#AsianDream -filter:retweets lang:en","#Football -filter:retweets lang:en","#car -filter:retweets lang:en","#apple -filter:retweets lang:en","microsoft -filter:retweets lang:en","dbrand -filter:retweets lang:en","bose -filter:retweets lang:en","#sony -filter:retweets lang:en","#canada -filter:retweets lang:en","#india -filter:retweets lang:en","#aib -filter:retweets lang:en","#dell -filter:retweets lang:en","#bike -filter:retweets lang:en","#travel -filter:retweets lang:en","#monday -filter:retweets lang:en","#tuesday -filter:retweets lang:en","#mondayblue -filter:retweets lang:en","#fly -filter:retweets lang:en","#ranveersingh -filter:retweets lang:en","#ranbirkapur -filter:retweets lang:en","#git -filter:retweets lang:en","#gitbucket -filter:retweets lang:en","#github -filter:retweets lang:en"]
with open ('Clean_file.csv','w') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['id', 'user', 'created_at', 'text'])
        for query in queries:
                t = get_tweets(query)
                for tweet in t:
                        tweet.text=' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",tweet.text).split())
                        writer.writerow([tweet.id_str,tweet.user.screen_name,tweet.created_at,tweet.text])
                        '''
                        1. Adpated above from : https://dev.to/rodolfoferro/sentiment-analysis-on-trumpss-tweets-using-python-
                        2. Adpated above from : https://stackoverflow.com/questions/8376691/how-to-remove-hashtag-user-link-of-a-tweet-using-regular-expression
                        '''