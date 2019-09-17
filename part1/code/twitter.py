"""
Twitter data sourcing
"""
from twython import TwythonStreamer
from twython import Twython
import csv
import pandas as pd
import time


credentials = {}
credentials['CONSUMER_KEY'] = "<PATE_YOUR_API_KEY>"
credentials['CONSUMER_SECRET'] = "<PASTE_YOUR_API_KEY>"

tweets = Twython(credentials['CONSUMER_KEY'], credentials['CONSUMER_SECRET'])

iterations = 0
count2 = 93

dict_ = {'user': [], 'date': [], 'text': [], 'favorite_count': [], 'location': []}
# df = pd.DataFrame(dict_)

while iterations <= 12000:
    query = {'q': '#AI OR #ArtificialIntelligence OR #MachineLearning OR #DeepLearning OR #SelfDrivingCar OR #ReinforcementLearning OR #DeepMind OR #Google OR AI OR Artificial Intelligence OR Machine Learning OR Deep Learning OR Self Driving Car OR Reinforcement Learning OR Elon Musk OR Andrew NG OR DeepMind OR Google', \
             'count': 1000, 'lang': 'en'}

    for status in tweets.search(**query)['statuses']:
        if status['user']['location'] != '':
            dict_['user'].append(status['user']['screen_name'])
            dict_['date'].append(status['created_at'])
            dict_['text'].append(status['text'])
            dict_['favorite_count'].append(status['favorite_count'])
            dict_['location'].append(status['user']['location'])

    iterations += 1

    if iterations % 300 == 0:
        df = pd.DataFrame(dict_)
        dict_ = {'user': [], 'date': [], 'text': [], 'favorite_count': [], 'location': []}
        df.to_csv('tweets'+str(count2)+'.csv')
        print('Sleeping after ' + str(iterations) + ' iterations')
        count2 += 1
        time.sleep(15*60)

"""
Twitter Data cleaning
"""
import os
import csv
import re

# Keept all tweets from above into one directory "tweets"
# Run below part to clean & remove redundant tweets

tweet_list = set()
for filename in os.listdir("tweets"):
    ls = 0
    if filename.endswith(".csv"):
        with open(os.path.join("tweets",filename), 'r',encoding="utf8") as file:
            csvreader = csv.reader(file)

            for row in csvreader:
                if ls==0:
                    ls=1
                    continue
                twt = row[3].replace("\n"," ")
                if twt not in tweet_list:
                    tweet_list.add(twt)
        print(filename," done")


# write clean tweets into tweet.txt file
fi = open("tweet.txt","w",encoding="utf8")
for twt in tweet_list:
    new_twt = ""
    twt = twt.lower()
    for ch in twt:
        if ord("a") <= ord(ch) <= ord("z"):
            new_twt += ch
        else:
            new_twt += " "
    new_twt = re.sub(' +', ' ',new_twt)
    fi.write(new_twt+"\n")
fi.close()