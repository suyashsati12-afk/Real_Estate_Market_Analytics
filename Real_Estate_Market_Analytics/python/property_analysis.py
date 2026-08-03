import pandas as pd

df = pd.read_csv("C:/Users/suyash/OneDrive/Desktop/Real_Estate_Market_Analytics/data/transactions_clean.csv")

print(df.head())

print("Transaction data loaded successfully")

print(df.describe())