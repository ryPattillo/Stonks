import finnhub
import time
from sklearn.model_selection import train_test_split
import numpy as np

'''
NOTE: here is a list of all the keys in the dataset
keys = [
    0 - "quarter", [x]
    1 - "stock", [x]
    2 - "date",
    3 - "open",
    4 - "high",
    5 - "low",
    6 - "close",
    7 - "volume",
    8 - "percent_change_price",
    9 - "percent_change_volume_over_last_wk"
    10 - "previous_weeks_volume",
    11 - "next_weeks_open",
    12 - "percent_change_next_weeks_price  [pcw] [y]
    13 - "days_to_next_dividend",
    14 - "percent_return_next_dividend"
]
'''


def get_data():

    numeric_idx = [0,3,4,5,6,7,8,13,14]
    finnhub_client = finnhub.Client(api_key="c004igf48v6v49v27a2g")

    #print(finnhub_client.company_profile2(symbol='AAPL'))

    '''
    Get dataset of x,y values
    '''
    # open data file
    try:
        stock_data = open("stock_data.txt","r")
    except:
        print("Error opening file")

    # the first row contains all the attribute names
    first_row = True

    y_values = []
    x_values = []

    calls = 0

    for entry in stock_data:
        if first_row:
            attributes = entry.split(',')
            first_row = False
            continue
    
        # if calls == 59:
        #     time.sleep(60)
        #     calls = 0


        values = entry.split(',')
        x_values.append(np.array([float(values[i]) for i in numeric_idx]))
        y_values.append(float(values.pop(12)))


        # # profile = finnhub_client.company_profile2(symbol=values[1])
        # if profile is not None:
        #     industry = profile['finnhubIndustry']
        #     print(industry)
        # calls += 1

        
    return np.array(x_values),np.array(y_values)/200,attributes


