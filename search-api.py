from twython import Twython
import json
import pandas as pd

# load credentials
with open('twitter_credentials.json','r') as file:
    creds = json.load(file)

# this will create the main object where methods will be called from
first_tweets = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])

# query
query = {
    'q':'iowa hawkeyes',
    'result_type':'popular',
    'count':10,
    'lang':'en'
}

# using the first_tweets object and query, create a dict and view it as a df

new_dict = {'user': [], 'date': [], 'text': [], 'favorite_count': []}
for status in first_tweets.search(**query)['statuses']:
    new_dict['user'].append(status['user']['screen_name'])
    new_dict['date'].append(status['created_at'])
    new_dict['text'].append(status['text'])
    new_dict['favorite_count'].append(status['favorite_count'])

# create df
df = pd.DataFrame(new_dict)
print(df.head())

