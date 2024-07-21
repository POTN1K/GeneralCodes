import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats

file = 'C:\\Users\\ricke\\Documents\\Python Docs\\cars.csv'
df = pd.read_csv(file)

print(df.dtypes)
print()
print(df.describe())

# Sustituye el simbolo por not available number
df.replace("?", np.nan, inplace=True)

# Cambia de tipo objeto a float/int
df["normalized-losses"] = df["normalized-losses"].astype(float)
df["price"] = df["price"].astype(float)
df['horse-power'] = df['horse-power'].astype(float)

# Elimina los que no tienen precio
df.dropna(subset=["price"], axis=0, inplace=True)

# Obtienes media y cambias los NaN a media
mean = df["normalized-losses"].mean()
df["normalized-losses"].replace(np.nan, mean, inplace=True)

# Pasar de mpg a L/100km
df["city-mpg"] = 235 / df["city-mpg"]
df["highway-mpg"] = 235 / df["highway-mpg"]
df.rename(columns={"city-mpg": "city-L/100km"}, inplace=True)
df.rename(columns={"highway-mpg": "highway-L/100km"}, inplace=True)

# Normalizar data
df["length"] = (df["length"] - df["length"].mean()) / df["length"].std()

# Binning- separar en rangos
bins = np.linspace(min(df["price"]), max(df["price"]), 4)
group_names = ["Low", "Medium", "High"]
df["price-binned"] = pd.cut(df["price"], bins, labels=group_names, include_lowest=True)

# One-hot encoding (Separa en otras columnas con numeros si es diesel o gas), no se ha agregado al df
pd.get_dummies(df["fuel type"])

# Descriptive Statistics
# Cuenta valores en una columna
drive_wheels_counts = df["drive wheels"].value_counts()
drive_wheels_counts.rename('value counts', inplace=True)
drive_wheels_counts.index.name = 'drive wheels'
print(drive_wheels_counts)

# Diagrama de caja y bigotes
sns.boxplot(x="drive wheels", y="price", data=df)
plt.show()

# Crea un diagrama de dispersion
y = df["price"]
x = df["engine size"]
plt.scatter(x, y)
plt.title("Scatterplot of Engine Size vs Price")
plt.xlabel("Engine Size")
plt.ylabel("Price")
plt.show()

# Agrupar (ve cual es mas caro de acuerdo al tipo de carro y llantas)
df_test = df[['drive wheels', 'body style', 'price']]
df_grp = df_test.groupby(['drive wheels', 'body style'], as_index=False).mean()
print(df_grp)

# Pivot te lo convierte en una tabla mas legible
df_pivot = df_grp.pivot(index='drive wheels', columns='body style')
print(df_pivot)

# Heat map (te lo divide en colores para que se vea mas facil)
plt.pcolor(df_pivot, cmap='RdBu')
plt.colorbar()
plt.show()

# Correlation (linear regression)
sns.regplot(x='engine size', y='price', data=df)
plt.ylim(0,)
plt.show()

# Obtener coeficientes de Pearson y p-value. No debe haber NaN
df.dropna(subset=["horse-power"], axis=0, inplace=True)
pearson_coef, p_value = stats.pearsonr(df['horse-power'], df['price'])
print(pearson_coef, p_value)

path = "C:\\Users\\ricke\\Documents\\Python Docs\\cars2.csv"
df.to_csv(path)
