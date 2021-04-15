import csv
import io
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
from scipy.stats import norm
from statistics import mean
import numpy as np
import seaborn as sns # very nice plotting package

from pprint import pprint
from pymongo import MongoClient #import the client from backend
client= MongoClient('mongodb+srv://steven:steven1234@cluster0.nqvov.mongodb.net/test?authSource=admin&replicaSet=atlas-116n91-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
filter={}

result = client['Market']['items']

data = []
for x in result.find():
  data.append(x)

df= pd.DataFrame.from_dict(data)
# CHANGE THE ITEM NAME HERE
##############################
item = "cabbage"
##############################

def algorithm(item):
    cabbage = df.loc[df.name == "cabbage"]
    lettuce = df.loc[df.name == "lettuce"]
    apple = df.loc[df.name == "apple"]
    banana = df.loc[df.name == "banana"]
    x_label='price'
    y_label='stars'
    if item == "cabbage":
        x=cabbage[x_label]
        y=cabbage[y_label]
    elif item == "apple":
        x=apple[x_label]
        y=apple[y_label]
    elif item == "lettuce":
        x=lettuce[x_label]
        y=lettuce[y_label]
    elif item =="banana":
        x=lettuce[x_label]
        y=lettuce[y_label]
    x_mean=np.mean(x)
    y_mean=np.mean(y)
    # print(x_mean, y_mean)
    # print(x)
    # print(y)
    y_good=[]
    # print("average stars : ", y_mean)

    for i in y:
        if i > y_mean:
            y_good.append(i)
    # print("above average quality groceries of all products : ", y_good)
    y_good_mean = np.mean(y_good)

    import statsmodels.api as statsmodels # useful stats package with regression functions
    def regression_model(column_x, column_y):
        # this function uses built in library functions to create a scatter plot,
        # plots of the residuals, compute R-squared, and display the regression eqn

        # fit the regression line using "statsmodels" library:
        X = statsmodels.add_constant(column_x)
        Y = column_y
        regressionmodel = statsmodels.OLS(Y,X).fit() #OLS = "ordinary least squares"
        
        # extract regression parameters from model, rounded to 3 decimal places:
        Rsquared = round(regressionmodel.rsquared,3)
        slope = round(regressionmodel.params[1],3)
        intercept = round(regressionmodel.params[0],3)
        
        # make plots:
        fig, (ax1, ax2) = plt.subplots(ncols=2, sharex=True, figsize=(12,4))
        sns.regplot(x=column_x, y=column_y, data=df, marker="+", ax=ax1) # scatter plot
        sns.residplot(x=column_x, y=column_y, data=df, ax=ax2) # residual plot
        ax2.set(ylabel='Residuals')
        ax2.set_ylim(min(regressionmodel.resid)-1,max(regressionmodel.resid)+1)
        plt.figure() # histogram
        sns.distplot(regressionmodel.resid, kde=False, axlabel='Residuals', color='red')
        
        # print the results:
        # print("R-squared = ",Rsquared)
        # print("Regression equation: y =",slope, "x + ",intercept)
        return slope, intercept

    def best_fit_yprediction(xvalue):
        return m*xvalue+b
    # print("prediction for 27, " ,best_fit_yprediction(27))

    def best_fit_xprediction(yvalue):
        return (yvalue-b)/m


    m,b= regression_model(x, y)
    # print("target quality of stars for product is : ", y_good_mean)
    # print("prediction for ", y_good_mean, " stars (customer price): ", best_fit_xprediction(y_good_mean))
    # print("prediction for employee target price : ", best_fit_xprediction(y_mean))
    return best_fit_xprediction(y_good_mean), best_fit_xprediction(y_mean)
customer_price, employee_target = algorithm(item)
print ("customer price for ",item," : ", customer_price)
print("employee target for ", item ," : ", employee_target)