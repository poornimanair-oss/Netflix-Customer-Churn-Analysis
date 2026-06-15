import pandas as pd

# Load dataset
df = pd.read_excel("netflix_large_user_data.xlsx")

# Rename columns
df.columns = [
    "Customer_ID",
    "Subscription_Length_Months",
    "Customer_Satisfaction_Score",
    "Daily_Watch_Time_Hours",
    "Engagement_Rate",
    "Device_Used_Most_Often",
    "Genre_Preference",
    "Region",
    "Payment_History",
    "Subscription_Plan",
    "Churn_Status",
    "Support_Queries_Logged",
    "Age",
    "Monthly_Income",
    "Promotional_Offers_Used",
    "Number_of_Profiles_Created"
]

print(df.head())

# Save cleaned data
df.to_csv("netflix_cleaned.csv", index=False)

print("Cleaned dataset saved successfully")