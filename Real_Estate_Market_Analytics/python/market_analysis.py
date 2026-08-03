import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/suyash/OneDrive/Desktop/Real_Estate_Market_Analytics/data/market_indicators_clean.csv")

print(df.head())

print("Market indicator data loaded successfully")

print(df.describe())


# simple visualization
df.plot(kind="bar", figsize=(10,5))

plt.title("Market Indicators Analysis")
plt.show()