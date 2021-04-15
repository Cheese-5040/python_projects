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

##############################
# "employeeId","itemId","amount","type", "district","category","price","storeId"
#this algo will calculate the price of the product given the above parameters
#in addition, it will feed the data back to predict the price of the product
#made by Chee Seng, 15/4/2021 for HackUST
##############################

def get_data():
    global babi
    client= MongoClient('mongodb+srv://steven:steven1234@cluster0.nqvov.mongodb.net/test?authSource=admin&replicaSet=atlas-116n91-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
    filter={}
    result = client['Market']['items']
    data = result.find()

    # df=pd.read_json(io.BytesIO(uploaded['dummy_json.json']))
    df= pd.DataFrame.from_dict(data)

    employeedf = df["employeeId"].unique()
    # employeedf = ['60759340913c1765b800a079']
    # print("employee babi",employeedf)

    #extract employee bargaining power
    employee_result = client['Market']['employees']
    employee_data=[]
    employee_data.append(employee_result.find())
    #convert curser to list of dictionaries
    list_cur = list(employee_data[0])

    # Converting to the JSON
    json_data = dumps(list_cur, indent = 2) 
    #convert to pandas dataframe
    babi= pd.read_json(json_data)
    babi["_id"]= pd.DataFrame(babi["_id"].values.tolist())

    bargPower=[]
    for i in range(len(df)):
      for j in range(len(babi)):
        if df['employeeId'][i] == babi['_id'][j]:
          bargPower.append(babi['bargPower'][j])
    df['bargPower']= bargPower
    # print(df.head)
    return df
# print(bargPower)

#convert request to numbers
def convert_request(request, request_Barg):
  # print(request)
  for i in range(len(request)):
    # print(df['category'][i])
    #category 
    if request[i] == "fruit":
      request[i]=int(0)
    elif request[i] == "veg":
      request[i]=int(1)
    elif request[i] == "poul":
      request[i]=int(2)
    elif request[i] ==  "dairy":
      request[i]=int(3)
    elif request[i] == "seafood":
      request[i]=int(4)
    elif request[i] == "cereals":
      request[i]=int(5)
    elif request[i] == "beverages":
      request[i]=int(6)
    #type
    elif request[i] == "discrete":
      request[i] = 1
    elif request[i] == "kg":
      request[i] = 0
    #district
    elif request[i] == "Mongkok":
      request[i] = 0
    elif request[i] == "Causeway Bay":
      request[i] = 1
    # print(request)
    #obtain the bargaining power from employee at employee database
    for j in range(len(babi)):
        if request[0] == babi['_id'][j]:
          request_Barg[0]=babi['bargPower'][j]
  return request_Barg

def setup():
  
    global X_train
    global X_test
    global y_train
    global y_test
    global regressor
    global sc
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
    for i in range(len(df)):
        if df['district'][i] == "Mongkok":
            df.at[i,'district']=int(0)
        elif df['district'][i] == "Causeway Bay":
            df.at[i,'district']=int(1)
    # print(df['district'][:5])
    df['type']=df['type'].eq('discrete').mul(1) #convert binary data to number 0 or 1
    df['storeId']= df['storeId'].astype(str)
    df['bargPower']= df['bargPower'].astype(float)
    df['category']= df['category'].astype(float)
    df['itemId']= df['itemId'].astype(float)
    df['amount']= df['amount'].astype(float)
    df['district']= df['district'].astype(float)
    df['type']= df['type'].astype(float)
    df['price']= df['price'].astype(float)

    price_titles = ["bargPower","itemId","amount","type", "district","category","price"]
    df1 = df.filter(price_titles)

    # a = df1.loc[df1["itemId"] == request_Barg[1]]
    
    X = df1.iloc[:, :6].values
    y = df1.iloc[:, 6].values
    # print(a.head(50))
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=0, shuffle=True)

    # Feature Scaling (scaling big numbers down so they influence will be less detrimental compared to others)
    sc = StandardScaler()
    # print(sc.fit_transform(X_train[:1]))
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)
    #make scaler for request_barg

    regressor = RandomForestRegressor(n_estimators=200, random_state=0)
    regressor.fit(X_train, y_train)
    y_pred = regressor.predict(X_test)
    # print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
    # print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
    # print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

def get_target_price(request_Barg):
    requestS= sc.transform([request_Barg])
    y_prediction = regressor.predict(requestS)
    # print("request_Barg",request_Barg)
    # print("requestS", requestS)
    return y_prediction[0]



#classification 
def store_init():
    global X_train2
    global X_test2
    global y_train2
    global y_test2
    global knn
    X2 = df.iloc[:, :7].values
    y2 = df.iloc[:, -1].values
    X_train2, X_test2, y_train2, y_test2 = train_test_split(X2, y2, test_size=0.5,random_state=0, shuffle = True)
    # training a KNN classifier
    from sklearn.neighbors import KNeighborsClassifier
    knn = KNeighborsClassifier(n_neighbors =9, weights='distance', algorithm='auto', leaf_size=30, p=1).fit(X_train2, y_train2)
    knn_predictions = knn.predict(X_test2) 

    # accuracy on X_test
    accuracyKnn = knn.score(X_test2, y_test2)
      
    # creating a confusion matrix
    # cmKnn = confusion_matrix(y_test2, knn_predictions)
    print("K nearest neighbour classifier accuracy : " , accuracyKnn)
    # sns.heatmap(cmKnn, center=True)
    # plt.show()

def init_program():
    global df
    df=get_data()
    print("babi")
    setup()
    # Request import & convert 
    columns_titles = [ "bargPower","itemId","amount","type", "district","category","price","storeId" ]
    df=df.reindex(columns=columns_titles) 
    store_init()



#insert call here
# "employeeId","itemId","amount","type", "district","category","price","storeId"
# {
#     _id: "blah",
#     itemId: "blah",
#     amount: 15,
#     type: 'discrete',
#     dsitrict: "Mongkok",
#     storeId: "babi"
# }
################
request = [[ '6076f6ccddc1145c187de178', 4,6,'kg', 'Mongkok','dairy'],[ '6076f6b8ddc1145c187de177', 0,1,'discrete', 'Mongkok','fruit']]
ori_request = []
request_Barg = request.copy()
###############
def get_target_and_store(request):
  ori_request = []
  request_Barg = request.copy()
  for i in range(len(request)):
    word = request[i].copy()
    # print(convert_request(request[i], request_Barg[i]))
    request_Barg[i]=convert_request(request[i], request_Barg[i])
    request_Barg[i].append(get_target_price(request_Barg[i]))
    # print("request_Barg", request_Barg[i])
    ori_request.append(word)
    prediction = knn.predict(request_Barg[i:i+1]) if i != len(request) else knn.predict(request_Barg[-1:])
    # print("store prediction : ", knn.predict(request_Barg[i:i+1]))
    ori_request[i].append(request_Barg[i][-1])
    ori_request[i].append(prediction[0])
  # print("ori_request : ", ori_request)
  return ori_request
# print(get_target_and_store(request))