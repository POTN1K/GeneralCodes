import pandas as pd

file = 'C:\\Users\\ricke\\Documents\\Python Docs\\imports-85.csv'
df = pd.read_csv(file, header=None)
headers = ["symboling", "normalized-losses", "make", "fuel type", "aspiration", "num of doors", "body style",
           "drive wheels",
           "engine location", "wheel base", "length", "width", "height", "curb weight", "engine type",
           "num of cylinders",
           "engine size", "fuel system", "bore", "stroke", "compression ratio", "horse-power", "peak rpm", "city-mpg",
           "highway-mpg", "price"]
df.columns = headers
print(df.head(5))
path = "C:\\Users\\ricke\\Documents\\Python Docs\\cars.csv"
df.to_csv(path)
