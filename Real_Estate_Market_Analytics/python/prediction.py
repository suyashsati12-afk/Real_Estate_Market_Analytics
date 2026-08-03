import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/suyash/OneDrive/Desktop/Real_Estate_Market_Analytics/data/price_forecast.csv")

print(df.head())

print("Forecast data loaded successfully")

print(df.describe())


# Forecast visualization
plt.figure(figsize=(10,5))

plt.plot(df.iloc[:,0], df.iloc[:,1])

plt.title("Future Property Price Forecast")
plt.xlabel("Time")
plt.ylabel("Predicted Price")

plt.xticks(rotation=45)

plt.show()