import pandas as pd

df = pd.read_excel("netflix_large_user_data.xlsx")

print(df.head())
print("\nColumns:")
print(df.columns.tolist())
print("========== DATA INFO ==========")
print(df.info())

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

print("\n========== SHAPE ==========")
print(df.shape)

print("\n========== DUPLICATES ==========")
print(df.duplicated().sum())

print("\n========== SUMMARY STATISTICS ==========")
print(df.describe())