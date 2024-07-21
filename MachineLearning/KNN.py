import itertools
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter
import pandas as pd
import matplotlib.ticker as ticker
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

# Obtain file
file = 'C:\\Users\\ricke\\Documents\\Python Docs\\teleCust1000t.csv'
df = pd.read_csv(file)

# Counts the number of each type of value
df['custcat'].value_counts()

# Visualization technique
df.hist(column='income', bins=50)
plt.show()

# Feature set. Changed from pandas to Numpy
X = df[['region', 'tenure', 'age', 'marital', 'address', 'income', 'ed', 'employ','retire', 'gender', 'reside']] .values
y = df['custcat'].values

# Normalize data
X = preprocessing.StandardScaler().fit(X).transform(X.astype(float))

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=4)
print('Train set:', X_train.shape,  y_train.shape)
print('Test set:', X_test.shape,  y_test.shape)

# KNN Classifier
k = 4
# Train Model
neigh = KNeighborsClassifier(n_neighbors=k).fit(X_train, y_train)
plt.show()
# Predict
yhat = neigh.predict(X_test)
# Accuracy evaluation
print("Train set Accuracy: ", metrics.accuracy_score(y_train, neigh.predict(X_train)))
print("Test set Accuracy: ", metrics.accuracy_score(y_test, yhat))
