'''
NOTE: here is a list of all the keys in the dataset
keys = [
    "quarter"
    "stock",
    "date",
    "open",
    "high",
    "low",
    "close",
    "volume",
    "percent_change_price",
    "percent_change_volume_over_last_wk",
    "previous_weeks_volume",
    "next_weeks_open",
    "percent_change_next_weeks_price",
    "days_to_next_dividend",
    "percent_return_next_dividend"
]
'''

def get_data():
    '''
    Get dataset of x,y values
    
    '''

    # open data file
    try:
        stock_data = open("stock_data.txt","r")
    except:
        print("Error opening file")

    # keep a list of the stock data

    # the first row contains all the attribute names
    first_row = True

    y_values = []
    x_values = []

    for entry in stock_data:
        if first_row:
            attributes = entry.split(',')
            first_row = False
            continue
    
        values = entry.split(',')
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