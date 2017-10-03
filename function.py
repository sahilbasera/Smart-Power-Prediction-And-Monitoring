from sklearn.ensemble import RandomForestRegressor
import pandas as pd
from sklearn.cross_validation import train_test_split



"""
This python file contains the logic and functions for the Smart Power Prediction And Monitoring

Note : while running the file in your device , keep dataset.csv and this python file in the same folder

"""

#To read data from the csv file
data = pd.read_csv('dataset.csv')


#features
X = data[['week']]

#labels
Y = data['power_used']


#To distribute data for training and testing the model
X_train , X_test , Y_train , Y_test = train_test_split( X , Y , test_size = 0.2 , random_state = 2)


# This specifies the type of machine learning model
reg = RandomForestRegressor()


#This fits the training data to that model
reg.fit(X_train , Y_train)


#This function displays the consumption predictions for a given user input
def make_pred(a):
   return reg.predict(a)


#This function displays the accuracy of the model
def accuracy():
    print("Accuracy of the model is : " +str(reg.score(X_test , Y_test)) + "\n")
    
