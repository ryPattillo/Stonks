import pandas as pd
from sklearn.preprocessing import OneHotEncoder
import numpy as np

def extract_data():
    df = pd.read_csv('data.csv')

    # get matrices of the columns
    values = df.to_numpy()

    # extract v_values
    y_values = values[:,12]

    # delete the y values
    # NOTE: just deleting these for now to test
    x_values = np.delete(values, 12, 1) 
    x_values = np.delete(x_values, 2, 1) 
    x_values = np.delete(x_values, 1, 1) 
    x_values = np.delete(x_values, 13, 1) 

    # convert to float
    x_values = x_values.astype(np.float32)
    y_values = y_values.astype(np.float32)

    # 1 if > 102 otherwise 0
    y_values = y_values * (y_values > 102)
    y_values[y_values > 0 ] = 1

    return x_values,y_values

