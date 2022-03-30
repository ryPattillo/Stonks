import finnhub
import time

'''
NOTE: here is a list of all the keys in the dataset
keys = [
    0 - "quarter",
    1 - "stock",
    2 - "date",
    3 - "open",
    4 - "high",
    5 - "low",
    6 - "close",
    7 - "volume",
    8 - "percent_change_price",
    9 - "percent_change_volume_over_last_wk", [pcw]
    10 - "previous_weeks_volume",
    11 - "next_weeks_open",
    12 - "percent_change_next_weeks_price",
    13 - "days_to_next_dividend",
    14 - "percent_return_next_dividend"
]
'''


def get_data():
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
    
        if calls == 59:
            time.sleep(60)
            calls = 0


        values = entry.split(',')
        profile = finnhub_client.company_profile2(symbol=values[1])
        if profile is not None:
            industry = profile['finnhubIndustry']
            print(industry)
        calls += 1

        
        x_values.append(values)
        y_values.append(values.pop(14))

    return x_values,y_values,attributes


def dataset_split(data,train_split,test_split,val_split):
    '''
    Split the datast into train,test, and val
    '''

    train_idx = int(train_split * len(data))
    test_idx = int(test_split * len(data))
    val_idx = int(val_split * len(data))

    train_data = data[0:train_idx]
    test_data = data[len(train_data) + 1: len(train_data) + test_idx + 1]
    val_data = data[len(test_data) + 1: len(test_data) + val_idx + 1]

    assert (len(train_data) + len(test_data) + len(val_data)) == (len(data) - 1)

    return train_data,test_data,val_data