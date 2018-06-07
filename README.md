# Data_Warehouse_Assignment_2

##  Sentiment Analysis of Twitter Tweet Data using ETL Process and Elastic Search

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
13. Sentiment Analysis 
```
```
14. Loading data into Elastic Search DB
```
```
















  



















   

   
