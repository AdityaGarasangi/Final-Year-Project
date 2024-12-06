import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load the dataset
df = pd.read_csv(r"E:\Final-Year-Project\AIFMS\static\data\MyTransaction.csv")

# Preprocess the data
df["Deposit"] = pd.to_numeric(df["Deposit"], errors="coerce").fillna(0)
df["Withdrawal"] = pd.to_numeric(df["Withdrawal"], errors="coerce").fillna(0)
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df = df.dropna(subset=["Date"])
df["Month"] = df["Date"].dt.to_period("M")
category_monthly = (
    df.groupby(["Month", "Category"])[["Deposit", "Withdrawal"]].sum().reset_index()
)
category_monthly["Spend"] = category_monthly["Withdrawal"]
category_monthly["Income"] = category_monthly["Deposit"]

# Add feature engineering
category_monthly["Prev_Spend"] = (
    category_monthly.groupby("Category")["Spend"].shift(1).fillna(0)
)
category_monthly["Spend_Change"] = (
    category_monthly["Spend"] - category_monthly["Prev_Spend"]
)


# Create target variable
def label_recommendation(row):
    if row["Spend_Change"] > 0 and row["Spend"] > 500:
        return "cut"
    elif row["Spend_Change"] < 0 and row["Income"] > 1000:
        return "increase"
    else:
        return "no_action"


category_monthly["recommendation"] = category_monthly.apply(
    label_recommendation, axis=1
)

# Features and target variable
X = category_monthly[["Income", "Spend", "Spend_Change"]]
y = category_monthly["recommendation"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train the model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# Save the model
joblib.dump(model, "recommendation_model.pkl")
