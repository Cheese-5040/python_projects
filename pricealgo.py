import numpy as np
import scipy
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
# pip install ppprint
from pprint import pprint
from pymongo import MongoClient #import the client from backend

#insert call here
################
request = ['chibabibabi',0 , 75309, 0,0, 1, 'discrete', 0,'']
###############

##############
client= MongoClient('mongodb+srv://steven:steven1234@cluster0.nqvov.mongodb.net/test?authSource=admin&replicaSet=atlas-116n91-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
filter={}

result = client['Market']['items']
data = []
for x in result.find():
  data.append(x)
#############

df= pd.DataFrame.from_dict(data)

def run_descision_tree(request):
    global df

    df.append(request)

    #convert categoties to numbers
    #key: fruit : 0, veg: 1, poul: 2, dairy: 3, seafood: 4, cereals: 5, beverages: 6 
    for i in range(len(df)):
        # print(df['category'][i])
        if df['category'][i] == "fruit":
            df.at[i,'category']=int(0)
        elif df['category'][i] == "veg":
            df.at[i,'category']=int(1)
        elif df['category'][i] == "poul":
            df.at[i,'category']=int(2)
        elif df['category'][i] == "dairy":
            df.at[i,'category']=int(3)
        elif df['category'][i] == "seafood":
            df.at[i,'category']=int(4)
        elif df['category'][i] == "cereals":
            df.at[i,'category']=int(5)
        elif df['category'][i] == "beverages":
            df.at[i,'category']=int(6)

    columns_titles = ["_id", "storeId","employeeId","category","itemId","amount", "type", "__v", "price"]
    df=df.reindex(columns=columns_titles)
    df['storeId']= df['storeId'].astype(float)
    df['employeeId']= df['employeeId'].astype(float)
    df['category']= df['category'].astype(float)
    df['itemId']= df['itemId'].astype(float)
    df['amount']= df['amount'].astype(float)
    df['price']= df['price'].astype(float)
    # print(df.dtypes)

    df.head()
    #data preprocessing
    a = df.loc[df["itemId"] == 0]
    b = df.loc[df["itemId"] == 1]
    c = df.loc[df["itemId"] == 2]
    d = df.loc[df["itemId"] == 3]
    # print(a.head(5))
    #select col of dataset to put into an array 
    if request[4] == 0:
        X = a.iloc[:, 1:6].values
        y = a.iloc[:, -1].values
    elif request[4] == 1:
        X = b.iloc[:, 1:6].values
        y = b.iloc[:, -1].values
    elif request[4] == 2:
        X = c.iloc[:, 1:6].values
        y = c.iloc[:, -1].values
    elif request[4] == 3:
        X = d.iloc[:, 1:6].values
        y = d.iloc[:, -1].values

    #split dataset for supervised learning 
    from sklearn.model_selection import train_test_split
    #change shuffle to true when we want more accurate predictions
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=0, shuffle=False)
    # print("X_test[-1] : ", X_test[-1])

    # Feature Scaling, scale to 1
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    # print(sc.fit_transform(X_train[:1]))
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    #supervised leaning algprothm
    from sklearn.ensemble import RandomForestRegressor
    regressor = RandomForestRegressor(n_estimators=200, random_state=0)
    regressor.fit(X_train, y_train)
    y_pred = regressor.predict(X_test)
    #prediction of target price
    # print("xtrain", X_test[-1])
    # print("request",request)
    y_prediction = regressor.predict(X_test[-1:])
    return y_prediction 
# #results
# from sklearn import metrics
# print(type(y_test[-1]), y_test[-1])
# print('Mean Absolute Error:', metrics.mean_absolute_error(y_test[:-2], y_pred[:-2]))
# print('Mean Squared Error:', metrics.mean_squared_error(y_test[:-2], y_pred[:-2]))
# print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test[:-2], y_pred[:-2])))
target_price= run_descision_tree(request)
print("target price employee : ", target_price)

