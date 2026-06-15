import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("netflix_cleaned.csv")

print(df.head())
print(df.shape)

df = pd.read_csv("netflix_cleaned.csv")
df["Churn_Status"].value_counts().plot(kind="bar")
plt.title("Customer Churn Distribution")
plt.show()

churn_device = pd.crosstab(
    df["Device_Used_Most_Often"],
    df["Churn_Status"])
churn_device.plot(kind="bar")
plt.title("Churn by Device")
plt.ylabel("Customers")
plt.show()
plan_churn = pd.crosstab(
    df["Subscription_Plan"],
    df["Churn_Status"])
plan_churn.plot(kind="bar")
plt.title("Churn by Subscription Plan")
plt.ylabel("Customers")
plt.show()
plt.hist(df["Age"], bins=20)
plt.title("Customer Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()
numeric_df = df.select_dtypes(include=["int64", "float64"])
plt.figure(figsize=(10, 6))
sns.heatmap(numeric_df.corr(), annot=True)
plt.title("Correlation Heatmap")
plt.show()