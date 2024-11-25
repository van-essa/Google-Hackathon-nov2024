# Import necessary libraries
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
from data_preprocessing import preprocess_data
from model_training import train_model
from model_evaluation import evaluate_model
from predict_sick_status import predict

# Step 1: Generate Synthetic Data (Only Run Once to Create Data)
def generate_synthetic_data():
    # Set a random seed for reproducibility
    np.random.seed(42)

    # Generate synthetic data for 50 employees over 90 days
    n_employees = 50
    n_days = 90
    start_date = datetime(2024, 1, 1)

    # Create a DataFrame for employees
    employee_ids = [f'EMP{str(i).zfill(3)}' for i in range(1, n_employees + 1)]
    dates = [start_date + timedelta(days=i) for i in range(n_days)]
    records = []

    # Generate data for each employee over each day
    for employee in employee_ids:
        for date in dates:
            sick_status = random.choice([0, 1])  # 0: available, 1: sick
            sick_history = random.randint(0, 5)  # Number of sick days in the past year
            seasonality = 1 if date.month in [11, 12, 1, 2] else 0  # Flu season in winter
            shift_info = random.choice(['Morning', 'Afternoon', 'Night'])  # Shift types
            location = random.choice(['North', 'South', 'East', 'West'])
            skill = random.choice(['Machine Operator', 'Maintenance', 'Technician'])
            labor_compliance = random.choice([True, False])  # Compliance with labor law

            # Append the generated record
            records.append([employee, date, sick_status, sick_history, seasonality, shift_info, location, skill, labor_compliance])

    # Create a DataFrame from the records
    df = pd.DataFrame(records, columns=['Employee_ID', 'Date', 'Sick_Status', 'Sick_History', 'Seasonality', 'Shift_Info', 'Location', 'Skill', 'Labor_Compliance'])

    # Save the dataset to a CSV file
    df.to_csv('synthetic_employee_data.csv', index=False)
    print("Synthetic data saved to 'synthetic_employee_data.csv'")

# Generate the synthetic data
generate_synthetic_data()

# Step 2: Load the generated dataset (now that it's created)
df = pd.read_csv('synthetic_employee_data.csv')

# Step 3: Preprocess the data
df_encoded, scaler = preprocess_data(df)

# Step 4: Split into features (X) and target (y)
X = df_encoded.drop(columns=['Employee_ID', 'Date', 'Sick_Status'])
y = df_encoded['Sick_Status']

# Step 5: Train the model
model = train_model(X, y)

# Step 6: Evaluate the model
accuracy, report = evaluate_model(model, X, y)
print(f"Accuracy: {accuracy}")
print(f"Classification Report: \n{report}")

# Step 7: Example: Predicting on new data
new_data = pd.DataFrame({
    'Sick_History': [0.2],
    'Seasonality': [0],
    'Shift_Info_Afternoon': [0],
    'Shift_Info_Night': [1],
    'Location_South': [1],
    'Skill_Maintenance': [0],
    'Labor_Compliance': [1],
})

# Pass the training set's columns to the predict function
prediction = predict(model, new_data, scaler, X.columns.tolist())
print(f"Prediction for new data: {prediction}")
