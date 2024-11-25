'''
This file will contain the prediction logic.
'''
import pandas as pd

def predict(model, new_data, scaler, expected_columns):
    # Ensure that new_data has the same columns as the training data (aligned and in the same order)
    
    # Add missing columns with value 0
    missing_cols = set(expected_columns) - set(new_data.columns)
    for col in missing_cols:
        new_data[col] = 0  # Set missing columns to 0

    # Remove extra columns that were not part of the training data
    new_data = new_data[expected_columns]
    
    # Ensure that the new data has the same order of columns as the training data
    new_data = new_data[expected_columns]
    
    # Scale the numerical columns (ensure it's done consistently)
    new_data_scaled = scaler.transform(new_data[['Sick_History', 'Seasonality']])

    # Predict the sick status
    prediction = model.predict(new_data)
    return prediction

