import numpy as np
import pandas as pd

import matplotlib.pyplot as plt


df = pd.read_csv('wine_quality.csv')
print(df.columns)
y = df['quality']
print(df.info())
features = df.drop(columns = ['quality'])



## 1. Data transformation
from sklearn.preprocessing import StandardScaler
standard_scaler_fit = StandardScaler().fit(features)
X = standard_scaler_fit.transform(features)



## 2. Train-test split
from sklearn.model_selection import train_test_split
X_train, y_train, X_test, y_test = train_test_split(X,y,test_size = 0.2, random_state = 99)

## 3. Fit a logistic regression classifier without regularization
from sklearn.linear_model import LogisticRegression

#Remember to set the penalty parameter to 'none'!
clf_no_reg = LogisticRegression(penalty = 'none')
clf_no_reg.fit(X_train, y_train)
## 4. Plot the coefficients


## 5. Training and test performance
from sklearn.metrics import f1_score
predictors = features.columns
coefficients = clf_no_reg.coef_.ravel()
coef = pd.Series(coefficients,predictors).sort_values()
coef.plot(kind='bar', title = 'Coefficients (no regularization)')
plt.tight_layout()
plt.show()
plt.clf()
## 6. Default Implementation (L2-regularized!)


## 7. Ridge Scores


## 8. Coarse-grained hyperparameter tuning
training_array = []
test_array = []
C_array = [0.0001, 0.001, 0.01, 0.1, 1]



## 9. Plot training and test scores as a function of C


## 10. Making a parameter grid for GridSearchCV


## 11. Implementing GridSearchCV with l2 penalty
from sklearn.model_selection import GridSearchCV


## 12. Optimal C value and the score corresponding to it


## 13. Validating the "best classifier"


## 14. Implement L1 hyperparameter tuning with LogisticRegressionCV
from sklearn.linear_model import LogisticRegressionCV


## 15. Optimal C value and corresponding coefficients



## 16. Plotting the tuned L1 coefficients
