import numpy as np
import scipy
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
# pip install ppprint
from pprint import pprint
from pymongo import MongoClient #import the client from backend
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.neighbors import KNeighborsClassifier

from bson.json_util import dumps


client= MongoClient('mongodb+srv://steven:steven1234@cluster0.nqvov.mongodb.net/test?authSource=admin&replicaSet=atlas-116n91-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
filter={}

result = client['Market']['items']

data = result.find()


# print(data)

# df=pd.read_json(io.BytesIO(uploaded['dummy_json.json']))
df= pd.DataFrame.from_dict(data)
# print(len(df))
# print(df.head())


columns_titles = [ "employeeId","itemId","amount","type", "district","category","price","storeId" ]
df=df.reindex(columns=columns_titles)
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
request = [ 123456, 0,2,'discrete', 1,'fruit',-1,-1]
###############
def convert_request(request):
    #convert request to numbers
    for i in range(len(request)):
    # print(df['category'][i])
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
        elif request[i] == "discrete":
            request[i] = 1
        elif request[i] == "continuous":
            request[i] = 0
    return request


def find_price(requestS):
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

    df['type']=df['type'].eq('discrete').mul(1) #convert binary data to number 0 or 1
    df['storeId']= df['storeId'].astype(float)
    df['employeeId']= df['employeeId'].astype(float)
    df['category']= df['category'].astype(float)
    df['itemId']= df['itemId'].astype(float)
    df['amount']= df['amount'].astype(float)
    df['district']= df['district'].astype(float)
    df['type']= df['type'].astype(float)
    df['price']= df['price'].astype(float)

    price_titles = ["employeeId","itemId","amount","type", "district","category","price"]
    df1 = df.filter(price_titles)

    a = df.loc[df["itemId"] == 0.0]
    b = df.loc[df["itemId"] == 1.0]
    c = df.loc[df["itemId"] == 2.0]
    d = df.loc[df["itemId"] == 3.0]
    # print(a.head(5))
    #select col of dataset to put into an array 
    #request 3 is the item that we want to predict price
    if request[1] == 0:
        X = a.iloc[:, :6].values
        y = a.iloc[:, 6].values
    elif request[1] == 1:
        X = b.iloc[:, :6].values
        y = b.iloc[:, 6].values
    elif request[1] == 2:
        X = c.iloc[:, :6].values
        y = c.iloc[:, 6].values
    elif request[1] == 3:
        X = d.iloc[:, :6].values
        y = d.iloc[:, 6].values

    # print(X[:5])

    # print(y[:5])
    a[-1:]

    from sklearn.model_selection import train_test_split
    #change shuffle to true when we want more accurate predictions
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=0, shuffle=True)
    # print(y_train[-1])
    # print( X_train[0])
    # print("request",X_test[-3:])
    # print("testing", X_train[0])

    # Feature Scaling

    sc = StandardScaler()
    # print(sc.fit_transform(X_train[:1]))
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)
    #make scaler for request
    requestS= sc.transform([[123456, 0,2,1, 1,0]])

    from sklearn.ensemble import RandomForestRegressor

    regressor = RandomForestRegressor(n_estimators=200, random_state=0)
    regressor.fit(X_train, y_train)
    y_pred = regressor.predict(X_test)
    # print("requestS", requestS)
    # print("request",request)
    y_prediction = regressor.predict(requestS)
    return y_prediction[0]

newRequest = convert_request(request)
print("request : ", request)
print("converted request: ", newRequest)
target = find_price(newRequest)
newRequest.append(target)
print("request with price : ", newRequest)

def find_store_in_district():
    #request[4] have the district location
    df2 = df.loc[df["district"]==request[4]]
    X2 = df2.iloc[:, :7].values
    y2 = df2.iloc[:, -1].values
    X_train2, X_test2, y_train2, y_test2 = train_test_split(X2, y2, test_size=0.5,random_state=0, shuffle = True)
    knn = KNeighborsClassifier(n_neighbors =8, weights='distance', algorithm='auto', leaf_size=30, p=1).fit(X_train2, y_train2)
    knn_predictions = knn.predict(X_test2) 

    # accuracy on X_test
    accuracyKnn = knn.score(X_test2, y_test2)
    
    # creating a confusion matrix
    cmKnn = confusion_matrix(y_test2, knn_predictions)
    print("K nearest neighbour classifier accuracy : " , accuracyKnn)
    sns.heatmap(cmKnn, center=True)
    plt.show()
    store_prediction = knn.predict() 
    print(X_test2[-1])
    print(store_prediction)