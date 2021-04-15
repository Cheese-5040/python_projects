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


#insert REQUEST HERE
################
# input = ["_id", "employeeId","category","itemId","amount", "type", "price"]
request = ['chibabibabi', 6681625, 0,2, 4, 'discrete', '']
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

    columns_titles = ["_id", "storeId","employeeId","category","itemId","amount", "district", "type", "__v", "price"]
    df=df.reindex(columns=columns_titles)
    df['_id']= df['_id'].astype(str)
    df['storeId']= df['storeId'].astype(float)
    df['employeeId']= df['employeeId'].astype(str)
    df['category']= df['category'].astype(float)
    df['itemId']= df['itemId'].astype(float)
    df['amount']= df['amount'].astype(float)
    df['district']= df['district'].astype(float)
    df['type']= df['type'].astype(str)
    df['price']= df['price'].astype(float)
    # print(df.dtypes)

    # split dataset to two df, df1 for price prediction, df for district prediction 
    price_titles = ["_id", "employeeId","category","itemId","amount","type", "price"]
    df1 = df.filter(price_titles)
    # print(request)


    #add request to dataframe1
    df1.loc[len(df)]=(request)
    # df1[-5:]
    ################

    a = df1.loc[df1["itemId"] == 0.0]
    b = df1.loc[df1["itemId"] == 1.0]
    c = df1.loc[df1["itemId"] == 2.0]
    d = df1.loc[df1["itemId"] == 3.0]
    # print(a.head(5))
    #select col of dataset to put into an array 
    #request 3 is the item that we want to predict price
    if request[3] == 0:
        X = a.iloc[:, 1:5].values
        y = a.iloc[:, -1].values
    elif request[3] == 1:
        X = b.iloc[:, 1:5].values
        y = b.iloc[:, -1].values
    elif request[3] == 2:
        X = c.iloc[:, 1:5].values
        y = c.iloc[:, -1].values
    elif request[3] == 3:
        X = d.iloc[:, 1:5].values
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
    ################## predicted price
    print(y_prediction)
    ##################    
    return y_prediction 


# classification
def optimal_store_prediction(request, target_price):
    global df

    columns_titles = ["_id","storeId","category","itemId","amount", "type", "price", "district"]
    df=df.reindex(columns=columns_titles)


    request[6] = target_price[0] #store the predicted price back into the price for district prediction
    request.append(-1)#add empty column to predict the district (dummy)
    #feeding the price back to the model to predict the district for the most optimal district to improve negotiation 
    df.loc[len(df)]=(request)
    df['type']=df['type'].eq('discrete').mul(1) #convert binary data to number 0 or 1
    # print(request)
    # print("empty columns: ", df.isnull().values.any())
    # print(df[-1:])
    columns_titles = ["category","itemId","amount", "type", "price", "district"]

    df2=df.reindex(columns=columns_titles)

    X2 = df2.iloc[:, :5].values
    y2 = df2.iloc[:, -1].values

    print("Request: ", X2[-1:])
    X_train2, X_test2, y_train2, y_test2 = train_test_split(X2, y2, test_size=0.2,random_state=None, shuffle = False)
    # training a KNN classifier
    from sklearn.neighbors import KNeighborsClassifier
    knn = KNeighborsClassifier(n_neighbors = 3, weights='uniform', algorithm='auto', leaf_size=30, p=3).fit(X_train2, y_train2)
    knn_predictions = knn.predict(X_test2) 

    # accuracy on X_test
    accuracyKnn = knn.score(X_test2, y_test2)
    
    # creating a confusion matrix
    cmKnn = confusion_matrix(y_test2, knn_predictions)
    # print("K nearest neighbour classifier accuracy : " , accuracyKnn)
    sns.heatmap(cmKnn, center=True)
    # plt.show()
    district_prediction = knn.predict(X_test2[-1:]) 
    return target_price[0], district_prediction[0]



target, district=optimal_store_prediction(request, run_descision_tree(request))
print("target_price: ", target)
print("district : ", district)
