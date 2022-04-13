#importing libraries 

import imp
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# importing dataset 
dataset = pd.read_csv('Data.csv')

#Seperating independent variable from dependent

X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values

# Handling the missing data
# take care of missing data in dataset

from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)

# To select columns from where we have to calculate data
imputer = imputer.fit(X[:,1:3])
# To make changes to the original dataset 

X[:,1:3] = imputer.transform(X[:,1:3])

# To deal with categorical data we had to convert it into numbers
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

labelencoder_x = LabelEncoder()

# Convertir first column into integer values
X[:,0] = labelencoder_x.fit_transform(X[:,0])
# Encoding categirucal data using one hot encoding
onehotencoder = OneHotEncoder(Categorical_featyres =  [0])

