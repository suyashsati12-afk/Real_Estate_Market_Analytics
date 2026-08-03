import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/suyash/OneDrive/Desktop/Real_Estate_Market_Analytics/data/price_history_clean.csv")

print(df.describe())

plt.figure(figsize=(10,5))

plt.plot(df["recorded_date"], df["listed_price"])

plt.title("Property Price Trend")
plt.xlabel("Date")
plt.ylabel("Price")

plt.xticks(rotation=45)

plt.show()