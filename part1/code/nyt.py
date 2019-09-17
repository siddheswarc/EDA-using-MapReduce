"""
NYT Download articles
"""

from nytimesarticle import articleAPI
import pandas as pd
import time
import re

api = articleAPI("<PASTE_YOUR_API_KEY>")

df = pd.DataFrame()

for i in range(1,10):
  articles = api.search(q="Artificial Intelligence",
                     begin_date=int("20180"+str(i)+"01"), end_date=int("20180"+str(i)+"28"))
  df = df.append(pd.DataFrame.from_dict(articles))
  time.sleep(60)

for i in range(10,13):
  articles = api.search(q="Artificial Intelligence",
                     begin_date=int("2018"+str(i)+"01"), end_date=int("2018"+str(i)+"28"))
  df = df.append(pd.DataFrame.from_dict(articles))
  time.sleep(60)


for i in range(1,4):
  articles = api.search(q="Artificial Intelligence",
                     begin_date=int("20190"+str(i)+"01"), end_date=int("20190"+str(i)+"28"))
  df = df.append(pd.DataFrame.from_dict(articles))
  time.sleep(60)

df.to_csv('NYT_ArtificialIntelligence.csv')

df = pd.DataFrame()

for i in range(1,10):
  articles = api.search(q="Machine Learning",
                     begin_date=int("20180"+str(i)+"01"), end_date=int("20180"+str(i)+"28"))
  df = df.append(pd.DataFrame.from_dict(articles))
  time.sleep(60)

for i in range(10,13):
  articles = api.search(q="Machine Learning",
                     begin_date=int("2018"+str(i)+"01"), end_date=int("2018"+str(i)+"28"))
  df = df.append(pd.DataFrame.from_dict(articles))
  time.sleep(60)

for i in range(1,4):
  articles = api.search(q="Machine Learning",
                     begin_date=int("20190"+str(i)+"01"), end_date=int("20190"+str(i)+"28"))
  df = df.append(pd.DataFrame.from_dict(articles))
  time.sleep(60)

df.to_csv('NYT_MachineLearning.csv')

df = pd.DataFrame()

for i in range(1,10):
  articles = api.search(q="Deep Learning",
                     begin_date=int("20180"+str(i)+"01"), end_date=int("20180"+str(i)+"28"))
  df = df.append(pd.DataFrame.from_dict(articles))
  time.sleep(60)

for i in range(10,13):
  articles = api.search(q="Deep Learning",
                     begin_date=int("2018"+str(i)+"01"), end_date=int("2018"+str(i)+"28"))
  df = df.append(pd.DataFrame.from_dict(articles))
  time.sleep(60)

for i in range(1,4):
  articles = api.search(q="Deep Learning",
                     begin_date=int("20190"+str(i)+"01"), end_date=int("20190"+str(i)+"28"))
  df = df.append(pd.DataFrame.from_dict(articles))
  time.sleep(60)

df.to_csv('NYT_DeepLearning.csv')

df = pd.DataFrame()

for i in range(1,10):
  articles = api.search(q="Self Driving Car",
                     begin_date=int("20180"+str(i)+"01"), end_date=int("20180"+str(i)+"28"))
  df = df.append(pd.DataFrame.from_dict(articles))
  time.sleep(60)

for i in range(10,13):
  articles = api.search(q="Self Driving Car",
                     begin_date=int("2018"+str(i)+"01"), end_date=int("2018"+str(i)+"28"))
  df = df.append(pd.DataFrame.from_dict(articles))
  time.sleep(60)

for i in range(1,4):
  articles = api.search(q="Self Driving Car",
                     begin_date=int("20190"+str(i)+"01"), end_date=int("20190"+str(i)+"28"))
  df = df.append(pd.DataFrame.from_dict(articles))
  time.sleep(60)

df.to_csv('NYT_SelfDrivingCar.csv')

df = pd.DataFrame()

for i in range(1,10):
  articles = api.search(q="Neural Network",
                     begin_date=int("20180"+str(i)+"01"), end_date=int("20180"+str(i)+"28"))
  df = df.append(pd.DataFrame.from_dict(articles))
  time.sleep(60)

for i in range(10,13):
  articles = api.search(q="Neural Network",
                     begin_date=int("2018"+str(i)+"01"), end_date=int("2018"+str(i)+"28"))
  df = df.append(pd.DataFrame.from_dict(articles))
  time.sleep(60)

for i in range(1,4):
  articles = api.search(q="Neural Network",
                     begin_date=int("20190"+str(i)+"01"), end_date=int("20190"+str(i)+"28"))
  df = df.append(pd.DataFrame.from_dict(articles))
  time.sleep(60)

df.to_csv('NYT_NeuralNetwork.csv')

df = pd.DataFrame()

for i in range(1,10):
  articles = api.search(q="Reinforcement Learning",
                     begin_date=int("20180"+str(i)+"01"), end_date=int("20180"+str(i)+"28"))
  df = df.append(pd.DataFrame.from_dict(articles))
  time.sleep(60)

for i in range(10,13):
  articles = api.search(q="Reinforcement Learning",
                     begin_date=int("2018"+str(i)+"01"), end_date=int("2018"+str(i)+"28"))
  df = df.append(pd.DataFrame.from_dict(articles))
  time.sleep(60)

for i in range(1,4):
  articles = api.search(q="Reinforcement Learning",
                     begin_date=int("20190"+str(i)+"01"), end_date=int("20190"+str(i)+"28"))
  df = df.append(pd.DataFrame.from_dict(articles))
  time.sleep(60)

df.to_csv('NYT_ReinforcementLearning.csv')

"""
NYT clean articles and store each paragraph in line
"""
from bs4 import BeautifulSoup
import requests
import os

# Collect nyt URLs from nyt sourcing
#
url_list = []
for filename in os.listdir("nyt"):
    ls = 0
    if filename.endswith(".csv"):
        print(filename)
        cnt=0
        with open(os.path.join("nyt",filename), 'r',encoding="utf8") as file:
            for line in file.readlines():
                for url in line.split("'"):
                    if "https://www.nytimes" in url:
                        url_list.append(url)
                        cnt += 1

url_list = (set(url_list))

# Visit all urls and write content in paratags
#
with open("nyt_paras.txt", "w") as nyt:
    for url in url_list:
        page = requests.get(str(url))
        soup = BeautifulSoup(page.text, 'html.parser')
        anchor_tags = soup.find_all('a')
        for tag in anchor_tags:
            para_tag = soup.find_all('p')
        for tag in para_tag:
            nyt.write(str(tag.prettify().encode("utf8"))+"\n")

# Clean data from paratags
#
with open("nyt_paras.txt","r") as nyt:
    with open("nyt_clean.txt","w") as clean:
        for line in nyt.readlines():
            s = ""
            line=line.lower()
            flag = False
            for ch in line:
                if ch == '<':
                    flag=True
                elif ch == '>':
                    flag=False
                if not flag and (ord('a')<=ord(ch)<=ord('z') or ch is ' '):
                    s += ch
            s = (re.sub(' +', ' ', s)).strip()

            if len(s)>0:
                clean.write(s+"\n")
