import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/price_forecast.csv")

df['month'] = pd.to_datetime(df['month'])

plt.figure(figsize=(12,5))

plt.plot(
    df['month'],
    df['avg_price'],
    label="Actual Price"
)

plt.plot(
    df['month'],
    df['forecast_price'],
    label="Forecast Price"
)

plt.xlabel("Month")
plt.ylabel("Price")

plt.title("Real Estate Price Trend and Forecast")

plt.legend()

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()