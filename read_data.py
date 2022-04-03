'''
This file is for reading data from the generated csv and 
converting into data that can be used by the model
'''
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler
import numpy as np

def extract_data():
    # get data from CSV
    df = pd.read_csv('data.csv')
    # get matrices of the columns
    values = df.to_numpy()

    # get the y_values
    y_values = values[:,13]

    # delete the y values
    x_values = np.delete(values, 13, 1) 

    # these rows are the ticker symbol, sector and date, not sure how we want to handle that  
    x_values = np.delete(x_values, 15, 1) 
    x_values = np.delete(x_values, 2, 1) 
    x_values = np.delete(x_values, 1, 1) 

    # convert to float
    x_values = x_values.astype(np.float32)
    y_values = y_values.astype(np.float32)

    # scale the x values using min max scaler
    scaler = MinMaxScaler()
    scaler = scaler.fit(x_values)
    x_values = scaler.transform(x_values)

    # TODO: one-hot encode the secotr column

    # seperate y values into appropriate classes
    y_classes = []

    for y in y_values:
        # BUY
        if y >= 1.00:
            classes = [1,0,0]
        # HOLD
        if y > -1.00 and y < 1.00: 
            classes = [0,1,0]
        # SELL
        if y < -1.00:  
            classes = [0,0,1]

        y_classes.append(classes)

    # reshape into from used by model
    y_classes = np.array(y_classes)
    y_classes = y_classes.reshape(len(y_values),3)
    return x_values,y_classes

