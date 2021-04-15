import numpy as np
import scipy
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn import metrics

import json
import seaborn as sns
import pandas as pd

# pip install ppprint
from pprint import pprint
from pymongo import MongoClient #import the client from backend
from bson.json_util import dumps
client= MongoClient('mongodb+srv://steven:steven1234@cluster0.nqvov.mongodb.net/test?authSource=admin&replicaSet=atlas-116n91-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
filter={}
result = client['Market']['items']
data = result.find()

# df=pd.read_json(io.BytesIO(uploaded['dummy_json.json']))
df= pd.DataFrame.from_dict(data)

import math
import random 
from statistics import mean 
item_average_market_rate = []
a= df.loc[df['itemId']=="0"]
b= df.loc[df['itemId']=="1"]
c= df.loc[df['itemId']=="2"]
d= df.loc[df['itemId']=="3"]
e= df.loc[df['itemId']=="4"]
f= df.loc[df['itemId']=="5"]
g= df.loc[df['itemId']=="6"]
h= df.loc[df['itemId']=="7"]
i= df.loc[df['itemId']=="8"]
j= df.loc[df['itemId']=="9"]
k= df.loc[df['itemId']=="10"]

######################## return this
item_average_market_rate = [mean(a["price"])+ random.random()*1.5,mean(b["price"])+ random.random()*1.5,mean(c["price"])+ random.random()*1.5,mean(d["price"])+ random.random()*1.5,mean(e["price"])+ random.random()*1.5,mean(f["price"])+ random.random()*1.5,mean(g["price"])+ random.random()*1.5,mean(h["price"])+ random.random()*1.5,mean(i["price"])+ random.random()*1.5,mean(j["price"])+ random.random()*1.5,mean(k["price"])+ random.random()*1.5]
########################
print(item_average_market_rate)
