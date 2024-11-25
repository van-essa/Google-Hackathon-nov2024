"""
Contains all the data loading and preprocessing functions.
"""
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def preprocess_data(df):
    df.fillna(0, inplace=True)
    df_encoded = pd.get_dummies(df, columns=['Shift_Info', 'Location', 'Skill'], drop_first=True)
    scaler = MinMaxScaler()
    df_encoded[['Sick_History', 'Seasonality']] = scaler.fit_transform(df_encoded[['Sick_History', 'Seasonality']])
    return df_encoded, scaler
