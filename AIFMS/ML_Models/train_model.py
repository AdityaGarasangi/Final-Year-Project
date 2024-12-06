import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
import joblib

# Load your dataset
df = pd.read_csv(r"E:\Final-Year-Project\AIFMS\static\data\MyTransaction.csv")

# Convert 'Date' column to datetime format, ensuring both formats are handled
df["Date"] = pd.to_datetime(
    df["Date"], format="%d/%m/%y", errors="coerce"
)  # Handles day/month/year format (13/01/23)
df["Date"] = pd.to_datetime(
    df["Date"], format="%d/%m/%Y", errors="coerce"
)  # Handles day/month/year format (1/2/2023)

# If there are invalid date formats, they will be converted to NaT
df = df.dropna(subset=["Date"])  # Drop rows with invalid date entries

# Extract year, month, and day as numeric features
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Day"] = df["Date"].dt.day

# Drop the original 'Date' column as it's no longer needed
df = df.drop(["Date", "Date.1"], axis=1)  # Drop both 'Date' and 'Date.1' if they exist

# Convert categorical 'Category' column to numerical format using one-hot encoding
df = pd.get_dummies(df, columns=["Category"], drop_first=True)

# Drop non-numeric columns, e.g., 'RefNo' (if necessary)
if "RefNo" in df.columns:
    df = df.drop(["RefNo"], axis=1)

# Check if there are any remaining columns that may cause issues
# Ensure all remaining columns are numeric or properly encoded
print(df.dtypes)  # This helps identify columns with unexpected types

# Set the target column name (update this to your actual target column)
target_column = "Balance"

# Check if the target column exists before proceeding
if target_column in df.columns:
    X = df.drop(target_column, axis=1)  # Features
    y = df[target_column]  # Target
else:
    print(f"Target column '{target_column}' not found in the DataFrame.")
    exit()

# Apply scaling only to numeric columns
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Use RandomForestRegressor for regression task
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_scaled, y)

# Save the model and scaler
joblib.dump(model, "model.pkl")
joblib.dump(scaler, "scaler.pkl")

print("Model and scaler saved successfully!")
