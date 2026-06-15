import pandas as pd

df = pd.read_csv("netflix_cleaned.csv")
df["Churn_Status"] = df["Churn_Status"].map({"Yes": 1,"No": 0})
print(df["Churn_Status"].value_counts())
df.drop("Customer_ID", axis=1, inplace=True)
df = pd.get_dummies(df, drop_first=True)
print(df.shape)
print(df.head())
print(df.columns)
X = df.drop("Churn_Status", axis=1)
y = df["Churn_Status"]
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print(X_train.shape)
print(X_test.shape)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)

X_test = scaler.transform(X_test)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression(max_iter=5000)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
rf = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
rf.fit(X_train, y_train)
rf_pred = rf.predict(X_test)
rf_accuracy = accuracy_score(y_test, rf_pred)
from sklearn.metrics import confusion_matrix

print(confusion_matrix(y_test, rf_pred))
feature_importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": rf.feature_importances_
})

print(
    feature_importance
    .sort_values(by="Importance", ascending=False)
    .head(10)
)

print("Random Forest Accuracy:", rf_accuracy)
