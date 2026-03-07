import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

data = pd.read_csv(r"C:\Users\DELL\Desktop\project\WA_Fn-UseC_-Telco-Customer-Churn.csv")

print("Dataset Preview:")
print(data.head())

data["TotalCharges"] = pd.to_numeric(data["TotalCharges"], errors="coerce")

data = data.dropna()


services = [
    "PhoneService",
    "MultipleLines",
    "OnlineSecurity",
    "OnlineBackup",
    "DeviceProtection",
    "TechSupport",
    "StreamingTV",
    "StreamingMovies"
]

for col in services:
    data[col] = data[col].replace({
        "Yes":1,
        "No":0,
        "No phone service":0,
        "No internet service":0
    }).infer_objects(copy=False)

data["TotalProducts"] = data[services].sum(axis=1)


start = int(input("Enter starting row: "))
end = int(input("Enter ending row: "))

print("\nSelected Customer Data:")
print(data.iloc[start:end][["customerID","TotalProducts"]])


data = data.drop("customerID", axis=1)

# Convert categorical data
data = pd.get_dummies(data, drop_first=True)

# Define features and target
X = data.drop("Churn_Yes", axis=1)
y = data["Churn_Yes"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LogisticRegression(max_iter=20000)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Accuracy
print("\nModel Accuracy:")
print(accuracy_score(y_test, y_pred))

# Classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6,4))
sns.heatmap(cm, annot=True, fmt="d")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()