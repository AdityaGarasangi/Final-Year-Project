import pandas as pd
import joblib

# Load the model and scaler
model = joblib.load("ML_Models/model.pkl")
scaler = joblib.load("ML_Models/scaler.pkl")

# Define the target column
target_column = "Balance"

# Define train_columns based on the training script
train_columns = [
    "Withdrawal",
    "Deposit",
    "Year",
    "Month",
    "Day",
    "Category_Misc",
    "Category_Salary",
    "Category_Shopping",
    "Category_Transport",
]


# Function to prepare new data for prediction
def prepare_new_data_for_prediction():
    # Assuming new_data is a DataFrame containing the new data to predict
    # For example, you could load it from a CSV file:
    # new_data = pd.read_csv("new_data.csv")

    # Example data (replace with your actual data)
    new_data = pd.DataFrame(
        {
            "Withdrawal": [100],
            "Deposit": [500],
            "Year": [2024],
            "Month": [12],
            "Day": [7],
            "Category_Misc": [0],
            "Category_Salary": [1],
            "Category_Shopping": [0],
            "Category_Transport": [0],
        }
    )

    # Ensure the columns match the training columns
    new_data = new_data[train_columns]

    # Apply the scaling used in training
    new_data_scaled = scaler.transform(new_data)

    return new_data_scaled


# Predict savings for next month
def predict_savings_for_next_month():
    new_data_scaled = prepare_new_data_for_prediction()
    prediction = model.predict(new_data_scaled)
    return prediction


# Get the prediction
predicted_savings = predict_savings_for_next_month()
print(f"Predicted savings for next month: {predicted_savings[0]:.2f}")
