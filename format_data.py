import finnhub
import time
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
from collections import defaultdict
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
# initialize finhub client
finnhub_client = finnhub.Client(api_key="c004igf48v6v49v27a2g")

# check to see if any empty values exist
def validate_data(values):
    for value in values:
        if value == '':
            return False
    return True

# get the sector for the ticker
def get_sector(ticker):
    profile = finnhub_client.company_profile2(symbol=ticker)  
    sector = ''
    if profile is not None:
        sector = profile['finnhubIndustry']
    return sector    
   
if __name__ == "__main__":
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
    stock_data_dict = defaultdict(list)
    api_calls = 0

    for row in stock_data:

        # first row are the column names
        if first_row:
            keys = row.split(',')
            # add the sector key as well
            keys.append("sector")
            first_row = False            
            continue

        # get the data
        values = row.split(',')

        # get the sector 
        #values.append(get_sector(values[1]))
        values.append("temp")
        api_calls += 1

        # only get 60 api calls a minute
        if api_calls == 59:
            api_calls = 0
            #time.sleep(60)

        # see if row needs to be ignored
        if not validate_data(values):
            continue
        # append data to the dictionary
        for i in range(len(keys)):
            key = keys[i]
            value = values[i]
            stock_data_dict[key].append(value)

    df = pd.DataFrame.from_dict(stock_data_dict)
    df.to_csv('data.csv', encoding='utf-8', index=False)

