import pandas as pd

df = pd.read_csv("data/price_forecast.csv")
print(df.head())

print("\nBasic Statistics:")
print(df.describe())

print("\nColumns:")
print(df.columns)

print("Analysis completed")