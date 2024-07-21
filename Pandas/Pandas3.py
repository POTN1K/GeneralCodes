import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import seaborn as sns
import matplotlib.pyplot as plt

file = 'C:\\Users\\ricke\\Documents\\Python Docs\\cars2.csv'
df = pd.read_csv(file)
print(df.dtypes)

# Crea objeto linear regression
lm = LinearRegression()

x = df[['highway-L/100km']]
y = df[['price']]

# Crea la linear regression
lm.fit(x, y)
Yhat = lm.predict(x)

# Te da la m y b
print(lm.intercept_)
print(lm.coef_)

# Modelo multivariable lineal
z = df[['horse-power', 'curb weight', 'engine size', 'highway-L/100km']]
lm.fit(z, df['price'])
z1 = lm.predict(z)
sns.regplot(x=z1, y=y)
plt.show()
